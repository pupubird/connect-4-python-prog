import GUI.Game_Logic.game_logic as logic
import curses
import GUI.Component.low_level_component as rectangle


buttons = []
# create based on saved record
log = logic.GameLogic()
_, _, sixseven_exists = log.load_saved_data('6:7')
_, _, sixnine_exists = log.load_saved_data('6:9')

if sixseven_exists:
    buttons.append("normal (6 x 7)")
if sixnine_exists:
    buttons.append("advance (6 x 9)")
buttons.append("return")


class ContinueGameOptions:
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

            if (key == curses.KEY_UP or key == 119 or key == 87) and current_button > 1:
                current_button -= 1

            elif (key == curses.KEY_DOWN or key == 115 or key == 83) and current_button < len(buttons):
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
        if current_button == buttons.index("return")+1:  # return
            import GUI.game_option as option_page
            option_page.OptionsPage(self.window)
        else:  # continue
            import GUI.game_board_page as board_page
            row = 6

            if "normal" in buttons[current_button-1]:
                col = 7
            elif "advance" in buttons[current_button - 1]:
                col = 9

            board_page.GameBoardPage(
                self.window, row, col, f"{row}:{col}", True)

    def clicking(self):
        import winsound
        winsound.PlaySound('./assets/music/clicking.wav',
                           winsound.SND_FILENAME)
