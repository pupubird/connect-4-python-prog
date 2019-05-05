import curses
from curses import panel
import snowterm
import game_board
import threading
import time


def main(window):
    window.border()
    window.addstr(11, 3, "wtfffffffffffffffffffffffffffff")

    window2 = curses.newwin(30, 150, 5, 7)

    window.refresh()
    window2.refresh()

    time.sleep(1)

    snow = threading.Thread(target=snowterm.main, args=[
                            window, 20], daemon=True)
    window_obj = threading.Thread(target=refreshwin, args=[window2])

    window_obj.start()
    snow.start()

    time.sleep(3)


def refreshwin(window):
    board = game_board.GameBoard(window, 5)
    while True:
        board.draw_board(5, 14)
        window.refresh()


curses.wrapper(main)
