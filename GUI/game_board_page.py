import curses
import threading
import time
import winsound
from GUI.Component import game_board
from GUI.Component import score_board
from GUI.Game_Logic import game_logic


def main(window, row_size, col_size):
    # play background music
    threading.Thread(target=play_background, daemon=True).start()

    curses.init_pair(1, curses.COLOR_YELLOW, 0)
    curses.curs_set(0)

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
        board_win = curses.newwin(40, 100, 7, 5)
        box_size = 5
    except Exception:
        board_win = curses.newwin(30, 100, 7, 5)
        box_size = 4
    _board(board_win, window, box_size, row_size, col_size)


def _board(window, orig_window, box_size, row_size, col_size):
    import threading
    board = game_board.GameBoard(window, box_size)
    board.draw_board(row_size, col_size)
    game_list = board.game_list
    # number(1,2,3..) key of curses, key 49 is 1, key 57 is 9
    number_key = [number for number in range(49, 58)]
    logic = game_logic.GameLogic()
    # game loop start
    isPlayer = True
    while True:
        # player turn
        if isPlayer:
            col_key = orig_window.getch()
            if col_key in number_key:
                # game logic checking
                valid_move, move_index = logic.slot_check(
                    game_list, number_key.index(col_key))
                if valid_move:
                    game_list[number_key.index(
                        col_key)][move_index].content = "O"
                    isPlayer = not isPlayer
                else:
                    # invalid move, show some message
                    pass
        # AI turn
        else:
            ai_index = _AI_move()
            valid_move, move_index = logic.slot_check(
                game_list, ai_index
            )
            if valid_move:
                game_list[number_key.index(
                    col_key)][move_index].content = "X"
                isPlayer = not isPlayer
            else:
                # unlikely to happen...but yea just in case
                pass
        curses.curs_set(0)
        board.refresh_board()


def clicking_music():
    winsound.PlaySound('./assets/music/clicking.wav', winsound.SND_ASYNC)


def play_background():
    winsound.PlaySound(
        '../assets/music/game_background.wav', winsound.SND_LOOP)


def _AI_move():
    # develop the AI move here, return the col_key
    return 1


def _score_board():
    score_win = curses.newwin(38, 35, 3, 128)
    score = score_board.ScoreBoard(score_win, 33, 35)
    score.draw_score_board()
