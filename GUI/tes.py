import curses
from Component import score_board
import time


def main(window):
    score = score_board.ScoreBoard(window, 10, 10)
    score.draw_score_board()
    window.refresh()
    time.sleep(3)


curses.wrapper(main)
