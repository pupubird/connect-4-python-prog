from curses import textpad
import curses
import time
from Component import low_level_component as component


def main(window):
    window.addch(curses.ACS_DIAMOND)
    window.refresh()
    time.sleep(3)


curses.wrapper(main)
