import curses
import time
import options_menu

buttons = ["Start", "Settings", "About", "Quit"]


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_button = 1
    height, width = stdscr.getmaxyx()

    def draw_menu():
        stdscr.clear()

        for string in buttons:
            if buttons.index(string)+1 == current_button:
                stdscr.addstr((height//2)-(len(buttons)//2)+buttons.index(string),
                              (width//2)-(len(string)//2), string, curses.color_pair(1))
            else:
                stdscr.addstr((height//2)-(len(buttons)//2) +
                              buttons.index(string), (width//2)-(len(string)//2), string)

        stdscr.refresh()

    while True:
        draw_menu()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_button > 1:
            current_button -= 1
        if key == curses.KEY_DOWN and current_button < 4:
            current_button += 1
        if key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, f"You pressed {buttons[current_button-1]}!")
            stdscr.refresh()
            key = stdscr.getch()
            if current_button == 2:
                stdscr.clear()
                options_menu.create_menu()
            if current_button == len(buttons):
                break

        draw_menu()


def create_menu():
    curses.wrapper(main)


# Prevent initialization of this file when imported by another.
if __name__ == "__main__":
    curses.wrapper(main)
