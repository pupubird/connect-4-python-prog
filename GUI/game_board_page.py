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
        curses.resize_term(49, 165)
        # play background music
        threading.Thread(target=self.play_background, daemon=True).start()
        self.window.refresh()
        curses.curs_set(0)

        self.window.addstr(
            7, 5, f"Please enter number 1-{self.col_size} to insert:              ")

        # draw the logo, set it to yellow colour
        curses.init_pair(1, curses.COLOR_YELLOW, 0)
        self.window.attron(curses.color_pair(1))
        state = 1 if self.game_mode == "6:7" else 2
        with open(f"./assets/ASCII_Art/logo{state}.txt", "r") as logo:
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
        logic = game_logic.GameLogic()
        import threading
        prompting_string = f"Please enter number 1-{self.col_size} to insert:              "
        invalid_string = f"invalid move, Please enter number 1-{self.col_size} to insert:"
        loading_string = f"Computer is thinking...  Autosaving                           "
        # total attemp counting
        self.total_attempt = 0
        self.window.addstr(
            40, 136, f"Total attempt: {self.total_attempt}")
        self.window.refresh()

        # board initialize
        board = game_board.GameBoard(board_window, box_size)
        board.draw_board(self.row_size, self.col_size)

        if self.game_mode == "6:7":
            win = 4
        else:
            win = 5
        board_window.addstr(
            31, 0, "How to Play:")
        board_window.addstr(
            32, 0, "Choose column 1-9, O is you and X is the opponent.")
        board_window.addstr(
            33, 0, "Objective: connect   horizontally, verticallly or diagonally to win")

        curses.init_pair(10, curses.COLOR_YELLOW, 0)
        board_window.attron(curses.color_pair(10))
        board_window.addstr(
            33, 19, f"{win}")
        board_window.attroff(curses.color_pair(10))

        board_window.refresh()

        # if continue game is true, load the data list, else, make a new list
        if self.load_saved:
            data, total_attempt, _ = logic.load_saved_data(self.game_mode)
            self.total_attempt = total_attempt
            board.data_set(data)
            board.refresh_board()
        else:
            logic.reset_data(self.game_mode)

        game_list = board.game_list

        # number(1,2,3..) key of curses, key 49 is 1, key 57 is 9
        number_key = [number for number in range(49, 58)]
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
                40, 136, f"Total attempt: {self.total_attempt}")

            # win check
            logic.save_data(board.data(),
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
        import AI.ai as ai
        col_key = random.choices([0,1,2,3,4,5,6])
        return col_key

    def clicking_music(self):
        winsound.PlaySound('../assets/music/clicking.wav', winsound.SND_ASYNC)

    def play_background(self):
        with open('./assets/data/config.json', 'r') as f:
            import json
            data = json.load(f)
            music = data[1]
        winsound.PlaySound(
            f'./assets/music/{music}.wav', winsound.SND_LOOP | winsound.SND_ASYNC)

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
            gameover_win, self.window, value, self.total_attempt, self.game_mode)
