import curses


def main(window):
    while True:
        key = window.getch()
        window.addstr(str(key))


curses.wrapper(main)
