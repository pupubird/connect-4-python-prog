import curses
import time
import main_menu

options = ["a", "b", "c", "d"]


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_option = 1
    height, width = stdscr.getmaxyx()

    def draw():
        for option in options:
            if options.index(option)+1 == current_option:
                stdscr.addstr(height//2-len(options)//2+options.index(option)+1,
                              width//2-len(option)//2, option, curses.color_pair(1))
            else:
                stdscr.addstr(height//2-len(options)//2 +
                              options.index(option)+1, width//2-len(option)//2, option)
        stdscr.refresh()

    while True:
        draw()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_option > 1:
            current_option -= 1
        if key == curses.KEY_DOWN and current_option < len(options):
            current_option += 1
        if key == curses.KEY_ENTER or key in [10, 13]:
            if current_option == len(options):
                stdscr.clear()
                stdscr.addstr(0, 0, "Quitting...")
                stdscr.refresh()
                time.sleep(1.5)
                main_menu.create_menu()

        stdscr.clear()


def create_menu():
    curses.wrapper(main)


if __name__ == "__main__":
    curses.wrapper(main)
