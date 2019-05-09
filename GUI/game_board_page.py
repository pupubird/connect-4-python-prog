import curses
import threading
import time
from GUI.Component import game_board


def main(window, win_width):
    # set the board size according to window screen
    _, win_width = window.getmaxyx()
    if win_width > 200:
        box_size = 6
    else:
        box_size = 5
    curses.curs_set(0)

    # draw the logo
    with open("assets\ASCII_Art\logo.txt", "r") as logo:
        logo_text = logo.readlines()
        for row in range(len(logo_text)):
            window.addstr(row, 5, logo_text[row])
    window.refresh()

    # draw the board
    board_win = curses.newwin(40, 150, 5, 5)
    _board(board_win, window, box_size)


def _board(window, orig_window, box_size):
    board = game_board.GameBoard(window, box_size)
    board.draw_board(6, 9)
    list = board.game_list
    while True:
        # under developing
        col_key = orig_window.getkey()
        try:
            list[int(col_key)].content = "0"
        except Exception:
            pass
        curses.curs_set(0)
        board.refresh_board()
