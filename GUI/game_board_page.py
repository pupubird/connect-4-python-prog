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
    board_thread = threading.Thread(target=_board, args=[board_win, box_size])
    board_thread.start()


def _board(window, box_size):
    board = game_board.GameBoard(window, box_size)
    board.draw_board(6, 9)
    while True:
        curses.curs_set(0)
        board.refresh_board()
