import curses
import time
from Component import low_level_component as component


def main(window):
    a = component.Rectangle(window)
    a.draw_rectangle(0, 0, 10, 10)
    window.refresh()
    time.sleep(4)


curses.wrapper(main)
