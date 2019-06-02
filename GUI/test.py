import curses
import time


def main(window):
    # Action in loop if resize is True:
    while True:
        key = window.getch()
        window.addstr(str(key))
        window.refresh()


curses.wrapper(main)
