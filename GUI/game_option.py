import curses
import GUI.Component.low_level_component as rectangle


buttons = ["New Game", "Continue"]


class OptionsPage:
    # new game or continue

    def __init__(self, window):
        self.window = window
        self.main()

    def main(self):
        current_button = 1

        while True:
            curses.curs_set(0)
            self.draw_menu(current_button)
            key = self.window.getch()

            if key == curses.KEY_UP or key == 119 and current_button > 1:
                current_button -= 1

            elif key == curses.KEY_DOWN or key == 115 and current_button < len(buttons):
                current_button += 1

            elif key == curses.KEY_ENTER or key in [10, 13]:
                self.clicking()
                self.window.clear()
                y, x = self.window.getmaxyx()
                board_win = curses.newwin(y, x)
                self.navigation(current_button)

    def draw_menu(self, current_button):
        self.window.clear()
        curses.resize_term(49, 165)

        width = 50
        height = 4
        start_y, start_x = 19, 55
        gap = 1
        for index, button in enumerate(buttons):
            if current_button == index+1:
                cur_btn = rectangle.Rectangle(
                    self.window, init_content=button, top_row=True, top_sym="X")
                cur_btn.draw_rectangle(
                    (height * index) + gap + start_y,
                    0 + start_x,
                    (height * (index + gap)) + start_y,
                    width + start_x)
            else:
                cur_btn = rectangle.Rectangle(
                    self.window, init_content=button)
                cur_btn.draw_rectangle(
                    (height * index) + gap + start_y,
                    0 + start_x,
                    (height * (index + gap)) + start_y,
                    width + start_x, False)

        self.window.refresh()

    def navigation(self, current_button):
        # navigate here
        if current_button == 1:  # new game
            import GUI.game_newgame as newgame_page
            newgame_page.NewGameOptions(self.window)

        elif current_button == 2:
            import GUI.game_continue_option as continue_page
            continue_page.ContinueGameOptions(self.window)

    def clicking(self):
        import winsound
        winsound.PlaySound('./assets/music/clicking.wav',
                           winsound.SND_FILENAME)
