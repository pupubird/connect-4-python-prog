import curses
import time

buttons = ["Start", "Leaderboards", "Options", "Quit"]
options = ["Option 1 [ ]", "Option 2 [ ]", "Option 3 [ ]", "Back"]
options_tog = ["Option 1 [X]", "Option 2 [X]", "Option 3 [X]", "Back"]
options_untog = ["Option 1 [ ]", "Option 2 [ ]", "Option 3 [ ]", "Back"]


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    height, width = stdscr.getmaxyx()
    current_button = current_menu = 1

    def draw_menu(current_menu):
        stdscr.clear()

        if current_menu == 1:
            for button in buttons:
                if buttons.index(button)+1 == current_button:
                    stdscr.addstr((height//2)-(len(buttons)//2)+buttons.index(button),
                                  (width//2)-(len(button)//2), button, curses.color_pair(1))
                else:
                    stdscr.addstr((height//2)-(len(buttons)//2) +
                                  buttons.index(button), (width//2)-(len(button)//2), button)

        if current_menu == 3:
            for option in options:
                if options.index(option)+1 == current_button:
                    stdscr.addstr((height//2)-(len(options)//2)+options.index(option),
                                  (width//2)-(len(option)//2), option, curses.color_pair(1))
                else:
                    stdscr.addstr((height//2)-(len(options)//2) +
                                  options.index(option), (width//2)-(len(option)//2), option)

        stdscr.refresh()

    while True:
        draw_menu(current_menu)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_button > 1:
            current_button -= 1

        if current_menu == 1:
            if key == curses.KEY_DOWN and current_button < len(buttons):
                current_button += 1
        if current_menu == 3:
            if key == curses.KEY_DOWN and current_button < len(options):
                current_button += 1

        if key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()

            if current_menu == 1:
                import GUI.game_board_page as board_page
                if current_button == 3:
                    current_menu = 3
                    current_button = 1
                if current_button == len(buttons):
                    break
                clicking()
                return board_page.GameBoardPage(stdscr, 6, 9, '6:9')

            elif current_menu == 3:
                if current_button != len(options):
                    stdscr.addstr(
                        0, 0, f"You toggled {options[current_button-1]}!")
                else:
                    stdscr.addstr(0, 0, "Returning...")
                if current_button == len(options):
                    current_button = 1
                    current_menu = 1
                else:
                    if '[X]' in options[current_button-1]:
                        options[current_button -
                                1] = options_untog[current_button-1]
                    else:
                        options[current_button -
                                1] = options_tog[current_button-1]

            stdscr.refresh()
            key = stdscr.getch()


def clicking():
    import winsound
    winsound.PlaySound('./assets/music/clicking.wav', winsound.SND_FILENAME)


if __name__ == "__main__":
    curses.wrapper(main)
