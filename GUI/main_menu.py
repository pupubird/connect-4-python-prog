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
        with open("./assets/ASCII_Art/logo1.txt", "r") as logo:
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
        with open("./assets/ASCII_Art/logo1.txt", "r") as logo:
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

        stdscr.addstr(
            36, 60, "Press W A S D to control, Enter to choose")
        stdscr.addstr(
            37, 60, "(or up and down key... XD)")
        stdscr.refresh()

    while True:

        curses.curs_set(0)
        draw_menu()
        key = stdscr.getch()
        # W A S D with capital considered
        if (key == curses.KEY_UP or key == 119 or key == 87) and current_button > 1:
            current_button -= 1

        if (key == curses.KEY_DOWN or key == 115 or key == 83) and current_button < len(buttons):
            current_button += 1

        if key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            y, x = stdscr.getmaxyx()
            board_win = curses.newwin(y, x)
            navigation(board_win, current_button)
            break


def navigation(stdscr, current_button):
    # navigate here
    import GUI.game_board_page as board_page
    import GUI.leaderboards_page as leader_boards_page
    import GUI.game_option as game_option_page
    import GUI.option_page as option_page
    import os
    import sys
    clicking()
    if current_button == 1:  # start

        game_option_page.OptionsPage(stdscr)

    elif current_button == 2:  # leaderboard
        leader_boards_page.LeaderBoardsPage(stdscr)

    elif current_button == 3:  # option
        option_page.OptionPage(stdscr)

    elif current_button == len(buttons):  # exit
        stdscr.clear()
        stdscr.refresh()
        sys.exit(0)


def clicking():
    import winsound
    winsound.PlaySound('./assets/music/clicking.wav', winsound.SND_FILENAME)


if __name__ == "__main__":
    curses.wrapper(main)
