import curses
from Component import low_level_component
import time


def main(window):
    a = low_level_component.Rectangle(window)
    a.draw_rectangle(0, 0, 10, 10)
    a.content = "A"
    a.color = curses.COLOR_YELLOW
    a.refresh_rectangle()
    b = low_level_component.Rectangle(window)
    b.draw_rectangle(0, 20, 10, 30)
    b.content = "B"
    b.color = curses.COLOR_YELLOW
    b.refresh_rectangle()
    window.refresh()
    time.sleep(1)
    b.content = "C"
    b.color = curses.COLOR_CYAN
    a.refresh_rectangle()
    b.refresh_rectangle()
    window.refresh()
    time.sleep(3)
    print(a, b)


curses.wrapper(main)
