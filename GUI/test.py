import curses


def main(window):
    window.border(0, 0)


curses.wrapper(main)
