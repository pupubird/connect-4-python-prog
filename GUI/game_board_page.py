import curses
import threading
import time
from GUI.Component import game_board
from GUI.Component import score_board


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

    # draw the game board
    try:
        board_win = curses.newwin(40, 90, 6, 5)
        box_size = 5
    except Exception:
        board_win = curses.newwin(30, 90, 6, 5)
        box_size = 4

    # draw the score board

    score_win = curses.newwin(40, 35, 3, 110)
    score = score_board.ScoreBoard(score_win, 33, 35)
    score.draw_score_board()

    _board(board_win, window, box_size, row_size, col_size)


def _board(window, orig_window, box_size, row_size, col_size):
    board = game_board.GameBoard(window, box_size)
    board.draw_board(row_size, col_size)
    game_list = board.game_list
    # number(1,2,3..) key of curses, key 49 is 1, key 57 is 9
    number_key = [number for number in range(49, 58)]
    # while True:
    #     # under developing
    #     col_key = orig_window.getch()

    #     if col_key in number_key:
    #         game_list[number_key.index(col_key)][-1].content = "O"
    #     curses.curs_set(0)
    #     board.refresh_board()
    time.sleep(3)
