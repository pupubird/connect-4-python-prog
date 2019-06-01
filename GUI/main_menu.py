import curses
import time
import GUI.Component.low_level_component as rectangle

buttons = ["Start", "Leaderboards", "Options", "Quit"]


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    height, width = stdscr.getmaxyx()
    current_button = 1

    def draw_menu():
        stdscr.clear()

        for button in buttons:
            if buttons.index(button)+1 == current_button:
                stdscr.addstr((height//2)-(len(buttons)//2)+buttons.index(button),
                              (width//2)-(len(button)//2), button, curses.color_pair(1))
            else:
                stdscr.addstr((height//2)-(len(buttons)//2) +
                              buttons.index(button), (width//2)-(len(button)//2), button)
        stdscr.refresh()

    while True:
        draw_menu()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_button > 1:
            current_button -= 1

        if key == curses.KEY_DOWN and current_button < len(buttons):
            current_button += 1

        # user choose, get the last key entered
        if key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()

            # direct menu here
            import GUI.game_board_page as board_page
            if current_button == 1:  # start
                clicking()
                return board_page.GameBoardPage(stdscr, 6, 9, '6:9')
            elif current_button == 2:  # leaderboard
                clicking()
                pass
            elif current_button == 3:  # options
                clicking()
                pass
            elif current_button == len(buttons):  # exit
                clicking()
                time.sleep(1)
                break

            stdscr.refresh()
            key = stdscr.getch()


def clicking():
    import winsound
    winsound.PlaySound('./assets/music/clicking.wav', winsound.SND_FILENAME)


if __name__ == "__main__":
    curses.wrapper(main)
