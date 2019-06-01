import curses
import time
import GUI.Component.low_level_component as rectangle

buttons = ["Start", "Leaderboards", "Options", "Quit"]


def main(stdscr):
    curses.curs_set(0)

    current_button = 1

    def draw_menu():
        stdscr.clear()

        width = 50
        height = 4
        start_y, start_x = 19, 55
        gap = 1
        for index, button in enumerate(buttons):
            if current_button == index+1:
                rectangle.Rectangle(stdscr, init_content=button, top_row=True, top_sym="X").draw_rectangle(
                    (height * index) + gap + start_y,
                    0 + start_x,
                    (height * (index + gap)) + start_y,
                    width + start_x)
            else:
                rectangle.Rectangle(stdscr, init_content=button).draw_rectangle(
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

            # navigate here
            import GUI.game_board_page as board_page
            clicking()
            if current_button == 1:  # start
                return board_page.GameBoardPage(stdscr, 6, 9, '6:9')
            elif current_button == 2:  # leaderboard
                pass
            if current_button == 3:  # option
                pass
            if current_button == len(buttons):  # exit
                break

            stdscr.refresh()
            key = stdscr.getch()


def clicking():
    import winsound
    winsound.PlaySound('./assets/music/clicking.wav', winsound.SND_FILENAME)


if __name__ == "__main__":
    curses.wrapper(main)
