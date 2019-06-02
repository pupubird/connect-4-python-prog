import curses
import threading
import time
import winsound
from GUI.Component import game_board
from GUI.Component import score_board
from GUI.Game_Logic import game_logic
from GUI.Component.low_level_component import LoadingAnimation
from Rules import rules


class GameBoardPage:
    def __init__(self, window, row_size, col_size, game_mode, load_saved=False):
        self.window = window
        self.row_size = row_size
        self.col_size = col_size
        self.game_mode = game_mode
        self.load_saved = load_saved
        self.main()

    def main(self):
        # play background music
        threading.Thread(target=self.play_background, daemon=True).start()
        self.window.refresh()
        curses.curs_set(0)

        self.window.addstr(
            7, 5, f"Please enter number 1-{self.col_size} to insert:              ")

        # draw the logo, set it to yellow colour
        curses.init_pair(1, curses.COLOR_YELLOW, 0)
        self.window.attron(curses.color_pair(1))
        with open("./assets/ASCII_Art/logo.txt", "r") as logo:
            logo_text = logo.readlines()
            for row in range(1, len(logo_text)+1):
                self.window.addstr(row, 5, logo_text[row-1])
        self.window.refresh()
        self.window.attroff(curses.color_pair(1))

        # draw the score board
        self._score_board()
        # draw the game board
        try:
            board_win = curses.newwin(40, 100, 8, 5)
            box_size = 5
        except Exception:
            board_win = curses.newwin(30, 100, 8, 5)
            box_size = 4
        self._board(board_win, box_size)

    def _board(self, board_window, box_size):
        import threading
        prompting_string = f"Please enter number 1-{self.col_size} to insert:              "
        invalid_string = f"invalid move, Please enter number 1-{self.col_size} to insert:"
        loading_string = f"Ai is thinking...                                          "
        # total attemp counting
        self.total_attempt = 0
        self.window.addstr(
            40, 136, f"Total attepmt: {self.total_attempt}")
        self.window.refresh()

        # board initialize
        board = game_board.GameBoard(board_window, box_size)
        board.draw_board(self.row_size, self.col_size)

        # if continue game is true, load the data list, else, make a new list
        if self.load_saved:
            data, total_attempt = self.load_saved_data()
            self.total_attempt = total_attempt
            board.data_set(data)

        game_list = board.game_list

        # number(1,2,3..) key of curses, key 49 is 1, key 57 is 9
        number_key = [number for number in range(49, 58)]
        logic = game_logic.GameLogic()
        # game loop start
        isPlayer = True
        while True:

            # player turn
            if isPlayer:
                col_key = self.window.getch()
                if col_key in number_key:
                    # game logic checking
                    valid_move, move_index = logic.slot_check(
                        game_list, number_key.index(col_key))
                    if valid_move:
                        # dropping animation
                        logic.dropping_animation(
                            board, game_list, number_key.index(col_key), move_index, "O")

                        isPlayer = not isPlayer
                        self.total_attempt += 1
                        self.window.addstr(7, 5, prompting_string)
                    else:
                        # invalid move, show some message
                        self.window.addstr(
                            7, 5, invalid_string)

            # AI turn
            else:
                ai_col = self._AI_move()
                valid_move, move_index = logic.slot_check(
                    game_list, ai_col
                )
                if valid_move:
                    # loading animation
                    self.window.addstr(7, 5, loading_string)
                    load = threading.Thread(
                        target=self.loading, args=[self.window])
                    load.start()
                    load.join()
                    curses.flushinp()

                    # dropping animation
                    logic.dropping_animation(
                        board, game_list, ai_col, move_index, "X")
                    isPlayer = not isPlayer
                    self.window.addstr(
                        7, 5, prompting_string)
                else:
                    # unlikely to happen...but yea just in case
                    self.window.addstr(
                        7, 5, invalid_string)

            # add total attempt to screen
            self.window.addstr(
                40, 136, f"Total attepmt: {self.total_attempt}")

            # win check
            logic.save_data('temp_board_data', board.data(),
                            self.game_mode, self.total_attempt)
            win_mode = 5 if self.game_mode == "6:9" else 4
            value, win_boo = rules.winning_check(
                win_mode, 'temp_board_data', self.game_mode)

            if win_boo:  # win

                # direct to gameover page
                self.clicking_music()
                self._gameover_page(value)
                break

            curses.curs_set(0)
            board.refresh_board()

    def _AI_move(self):
        import random
        # develop the AI move here, return the col_key
        col_key = random.choice([0, 1])
        return col_key

    def clicking_music(self):
        winsound.PlaySound('../assets/music/clicking.wav', winsound.SND_ASYNC)

    def play_background(self):
        winsound.PlaySound(
            './assets/music/game_background.wav', winsound.SND_LOOP | winsound.SND_ASYNC)

    def loading(self, window):
        animation = LoadingAnimation(window)
        animation.draw_loading(7, 40)

    def _score_board(self):
        score_win = curses.newwin(38, 50, 3, 110)
        score = score_board.ScoreBoard(score_win, 45, 35, self.game_mode)
        score.draw_score_board()

    def _gameover_page(self, value):

        import GUI.gameover_page as gameover_page
        gameover_win = curses.newwin(40, 99, 5, 40)
        gameover_page.GameOverPage(
            gameover_win, value, self.total_attempt, self.game_mode)
