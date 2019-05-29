import curses
import threading
import time
import winsound
from GUI.Component import game_board
from GUI.Component import score_board
from GUI.Game_Logic import game_logic
from GUI.Component.low_level_component import LoadingAnimation
from Rules import rules


def main(window, row_size, col_size):
    # play background music
    threading.Thread(target=play_background, daemon=True).start()
    window.refresh()
    curses.init_pair(1, curses.COLOR_YELLOW, 0)
    curses.curs_set(0)

    window.addstr(
        7, 5, "Please enter number 1-9 to insert:              ")

    # draw the logo, set it to yellow colour
    window.attron(curses.color_pair(1))
    with open("assets\ASCII_Art\logo.txt", "r") as logo:
        logo_text = logo.readlines()
        for row in range(1, len(logo_text)+1):
            window.addstr(row, 5, logo_text[row-1])
    window.refresh()
    window.attroff(curses.color_pair(1))

    # draw the score board
    _score_board()
    # draw the game board
    try:
        board_win = curses.newwin(40, 100, 8, 5)
        box_size = 5
    except Exception:
        board_win = curses.newwin(30, 100, 8, 5)
        box_size = 4
    _board(board_win, window, box_size, row_size, col_size)


def _board(window, orig_window, box_size, row_size, col_size):
    import threading
    # total attemp counting
    total_attempt = 0
    orig_window.addstr(
        40, 136, f"Total attepmt: {total_attempt}")
    orig_window.refresh()

    # board initialize
    board = game_board.GameBoard(window, box_size)
    board.draw_board(row_size, col_size)
    game_list = board.game_list

    # number(1,2,3..) key of curses, key 49 is 1, key 57 is 9
    number_key = [number for number in range(49, 58)]
    logic = game_logic.GameLogic()
    # game loop start
    isPlayer = True
    while True:

        save_data(board.data())
        # player turn
        if isPlayer:
            col_key = orig_window.getch()
            if col_key in number_key:
                # game logic checking
                valid_move, move_index = logic.slot_check(
                    game_list, number_key.index(col_key))
                if valid_move:
                    # dropping animation
                    logic.dropping_animation(
                        board, game_list, number_key.index(col_key), move_index, "O")

                    isPlayer = not isPlayer
                    total_attempt += 1
                    orig_window.addstr(
                        7, 5, "Please enter number 1-9 to insert:              ")

                else:
                    # invalid move, show some message
                    orig_window.addstr(
                        7, 5, "invalid move, Please enter number 1-9 to insert:")

                orig_window.addstr(
                    40, 136, f"Total attepmt: {total_attempt}")
                orig_window.refresh()
        # AI turn
        else:
            ai_col = _AI_move()
            valid_move, move_index = logic.slot_check(
                game_list, ai_col
            )
            if valid_move:
                # loading animation
                load = threading.Thread(target=loading, args=[orig_window])
                load.start()
                load.join()
                curses.flushinp()

                # dropping animation
                logic.dropping_animation(
                    board, game_list, ai_col, move_index, "X")
                isPlayer = not isPlayer
                orig_window.addstr(
                    7, 5, "Please enter number 1-9 to insert:              ")
            else:
                # unlikely to happen...but yea just in case
                orig_window.addstr(
                    7, 5, "invalid move, Please enter number 1-9 to insert:")

        # win check
        save_data(board.data())
        value, win_boo = rules.winning_check(5)
        if win_boo:
            # do something here, gameover page
            if value == "O":
                orig_window.addstr(
                    7, 5, "congrats! you win!                               ")
            elif value == "X":
                orig_window.addstr(
                    7, 5, "sorry! you lose!                                 ")

            orig_window.refresh()
            time.sleep(5)
            break

        curses.curs_set(0)
        board.refresh_board()


def _AI_move():
    import random
    # develop the AI move here, return the col_key
    col_key = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    return col_key


def clicking_music():
    winsound.PlaySound('../assets/music/clicking.wav', winsound.SND_ASYNC)


def play_background():
    winsound.PlaySound(
        '../assets/music/game_background.wav', winsound.SND_LOOP)


def loading(window):
    animation = LoadingAnimation(window)
    animation.draw_loading(7, 40)


def _score_board():
    score_win = curses.newwin(38, 35, 3, 128)
    score = score_board.ScoreBoard(score_win, 33, 35)
    score.draw_score_board()


def save_data(game_list):
    import json
    with open('./assets/data/board_data.json', 'w') as f:
        data = {'6:9': game_list}
        json.dump(data, f, indent=2)
