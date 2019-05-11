import curses
import threading
import time
from GUI.Component import game_board


def main(window, row_size, col_size):

    curses.init_pair(1, curses.COLOR_YELLOW, 0)
    # set the board size according to window screen
    _, win_width = window.getmaxyx()
    curses.curs_set(0)

    # draw the logo, set it to yellow colour
    window.attron(curses.color_pair(1))
    with open("assets\ASCII_Art\logo.txt", "r") as logo:
        logo_text = logo.readlines()
        for row in range(len(logo_text)):
            window.addstr(row, 5, logo_text[row])
    window.refresh()
    window.attroff(curses.color_pair(1))

    # draw the board
    try:
        board_win = curses.newwin(40, 150, 6, 5)
        box_size = 5
    except Exception:
        board_win = curses.newwin(30, 150, 6, 5)
        box_size = 4
    _board(board_win, window, box_size, row_size, col_size)


def _board(window, orig_window, box_size, row_size, col_size):
    curses.init_pair(2, curses.COLOR_GREEN, 0)
    curses.init_pair(3, curses.COLOR_BLUE, 0)
    board = game_board.GameBoard(window, box_size)
    board.draw_board(row_size, col_size)
    list = board.game_list
    # number key of curses, key 49 is 1, key 57 is 9
    number_key = [number for number in range(49, 58)]
    while True:
        # under developing
        col_key = orig_window.getch()

        if col_key in number_key:
            list[number_key.index(col_key)][-1].content = "O"
        curses.curs_set(0)
        board.refresh_board()
