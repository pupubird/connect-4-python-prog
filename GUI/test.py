import curses
import time


def main(screen):
    # Action in loop if resize is True:
    while True:
        y, x = screen.getmaxyx()
        screen.clear()
        screen.addstr(y // 2, x // 2, str(x))
        screen.refresh()
        curses.resize_term(49, 165)


curses.wrapper(main)
