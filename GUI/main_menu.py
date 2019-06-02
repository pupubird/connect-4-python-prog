import curses
import time
import GUI.Component.low_level_component as rectangle

buttons = ["Start", "Leaderboards", "Options", "Quit"]


def main(stdscr):
    curses.curs_set(0)
    current_button = 1

    for i in range(1, 9):
        # logo drop down animation
        stdscr.clear()
        curses.init_pair(1, curses.COLOR_YELLOW, 0)
        stdscr.attron(curses.color_pair(1))
        with open("./assets/ASCII_Art/logo.txt", "r") as logo:
            logo_text = logo.readlines()
            for row in range(1, len(logo_text)+1):
                stdscr.addstr(row+i, 52, logo_text[row-1])
        stdscr.refresh()
        stdscr.attroff(curses.color_pair(1))
        time.sleep(0.1)

    def draw_menu():

        curses.resize_term(49, 165)
        stdscr.clear()
        curses.curs_set(0)
        # draw logo
        curses.init_pair(1, curses.COLOR_YELLOW, 0)
        stdscr.attron(curses.color_pair(1))
        with open("./assets/ASCII_Art/logo.txt", "r") as logo:
            logo_text = logo.readlines()
            for row in range(1, len(logo_text)+1):
                stdscr.addstr(row+i, 52, logo_text[row-1])
        stdscr.refresh()
        stdscr.attroff(curses.color_pair(1))

        width = 50
        height = 4
        start_y, start_x = 19, 55
        gap = 1
        for index, button in enumerate(buttons):
            if current_button == index+1:
                cur_btn = rectangle.Rectangle(
                    stdscr, init_content=button, top_row=True, top_sym="X")
                cur_btn.draw_rectangle(
                    (height * index) + gap + start_y,
                    0 + start_x,
                    (height * (index + gap)) + start_y,
                    width + start_x)
            else:
                cur_btn = rectangle.Rectangle(
                    stdscr, init_content=button)
                cur_btn.draw_rectangle(
                    (height * index) + gap + start_y,
                    0 + start_x,
                    (height * (index + gap)) + start_y,
                    width + start_x, False)

        stdscr.refresh()

    while True:

        curses.curs_set(0)
        draw_menu()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_button > 1:
            current_button -= 1

        if key == curses.KEY_DOWN and current_button < len(buttons):
            current_button += 1

        if key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            y, x = stdscr.getmaxyx()
            board_win = curses.newwin(y, x)
            navigation(board_win, current_button)


def navigation(stdscr, current_button):
    # navigate here
    import GUI.game_board_page as board_page
    import os
    import sys
    clicking()
    if current_button == 1:  # start

        try:
            board_page.GameBoardPage(stdscr, 6, 7, '6:7')
        except Exception:
            input("Please maximize your screen to continue")
            navigation(stdscr, current_button)

    elif current_button == 2:  # leaderboard
        pass
    if current_button == 3:  # option
        pass
    if current_button == len(buttons):  # exit
        stdscr.clear()
        stdscr.refresh()
        sys.exit(0)

    os.system('python app.py')  # restart the program


def clicking():
    import winsound
    winsound.PlaySound('./assets/music/clicking.wav', winsound.SND_FILENAME)


if __name__ == "__main__":
    curses.wrapper(main)
