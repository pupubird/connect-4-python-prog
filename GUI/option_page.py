import curses
import GUI.Component.low_level_component as rectangle
buttons = ["Music", "Game board color", "Save"]
music_list = [" Music 1 ", " Music 2 ", " Music 3 "]
color_list = [" Yellow ", " Cyan ", "  Red  "]


class OptionPage:
    def __init__(self, window):
        self.window = window
        self.main()

    def main(self):
        curses.resize_term(49, 165)
        current_button = 1
        current_music = 1
        current_color = 1

        def draw_options(current_button, current_music, current_color):
            self.window.addstr(
                13, 60, "Press W A S D to control, ENTER to preview")

            if current_button == 1:
                music = rectangle.Rectangle(
                    self.window, top_row=True, top_sym=buttons[0])
                music.content = music_list[current_music - 1]
                music.draw_rectangle(15, 43, 20, 118)
                self.window.addstr(18, 39, "<")
                self.window.addstr(18, 122, ">")
                self.window.addstr(28, 39, " ")
                self.window.addstr(28, 122, " ")

                color = rectangle.Rectangle(
                    self.window, top_row=True, top_sym=buttons[1])
                color.content = color_list[current_color-1]
                color.draw_rectangle(25, 43, 30, 118, False)
                self.window.addstr(18, 41, " ")
                self.window.addstr(18, 120, " ")
                self.window.addstr(28, 41, "<")
                self.window.addstr(28, 120, ">")

                save = rectangle.Rectangle(self.window)
                save.content = buttons[2]
                save.draw_rectangle(33, 74, 37, 86, False)

            elif current_button == 2:
                color = rectangle.Rectangle(
                    self.window, top_row=True, top_sym=buttons[1])
                color.content = color_list[current_color-1]
                color.draw_rectangle(25, 43, 30, 118)
                self.window.addstr(18, 41, "<")
                self.window.addstr(18, 120, ">")
                self.window.addstr(28, 41, " ")
                self.window.addstr(28, 120, " ")

                music = rectangle.Rectangle(
                    self.window, top_row=True, top_sym=buttons[0])
                music.content = music_list[current_music - 1]
                music.draw_rectangle(15, 43, 20, 118, False)
                self.window.addstr(18, 39, " ")
                self.window.addstr(18, 122, " ")
                self.window.addstr(28, 39, "<")
                self.window.addstr(28, 122, ">")

                save = rectangle.Rectangle(self.window)
                save.content = buttons[2]
                save.draw_rectangle(33, 74, 37, 86, False)

            elif current_button == 3:
                save = rectangle.Rectangle(
                    self.window, top_row=True, top_sym="X")
                save.content = buttons[2]
                save.draw_rectangle(33, 74, 37, 86)

                color = rectangle.Rectangle(
                    self.window, top_row=True, top_sym=buttons[1])
                color.content = color_list[current_color-1]
                color.draw_rectangle(25, 43, 30, 118, False)

                music = rectangle.Rectangle(
                    self.window, top_row=True, top_sym=buttons[0])
                music.content = music_list[current_music - 1]
                music.draw_rectangle(15, 43, 20, 118, False)

                self.window.addstr(18, 41, "<")
                self.window.addstr(18, 120, ">")
                self.window.addstr(28, 41, "<")
                self.window.addstr(28, 120, ">")

                self.window.addstr(18, 39, " ")
                self.window.addstr(18, 122, " ")
                self.window.addstr(28, 39, " ")
                self.window.addstr(28, 122, " ")

            self.window.refresh()

        while True:
            curses.curs_set(0)
            draw_options(current_button, current_music, current_color)
            key = self.window.getch()
            disrupt_music()
            if key == curses.KEY_UP or key == 119 or key == 87 and current_button > 1:
                current_button -= 1

            elif key == curses.KEY_DOWN or key == 115 or key == 83 and current_button < len(buttons):
                current_button += 1
            elif key == 97 or key == curses.KEY_LEFT:  # left
                if current_button == 1:
                    if current_music > 1:
                        current_music -= 1
                    else:
                        pass
                elif current_button == 2:
                    if current_color > 1:
                        current_color -= 1
                    else:
                        pass
            elif key == 100 or key == curses.KEY_RIGHT:  # right
                if current_button == 1:
                    if current_music < len(music_list):
                        current_music += 1
                    else:
                        pass
                elif current_button == 2:
                    if current_color < len(color_list):
                        current_color += 1
                    else:
                        pass
            elif key == curses.KEY_ENTER or key in [10, 13]:
                clicking()
                # music preview
                if current_button == 1:
                    play_music(current_music)
                elif current_button == 3:
                    save_configuration(current_color, current_music)
                    import app
                    app.main(self.window)


def clicking():
    import winsound
    winsound.PlaySound('./assets/music/clicking.wav',
                       winsound.SND_FILENAME)


def disrupt_music():
    import winsound
    winsound.PlaySound(None, winsound.SND_FILENAME)


def play_music(current_music):
    import winsound
    winsound.PlaySound(f'./assets/music/game_background{current_music}.wav',
                       winsound.SND_ASYNC)


def save_configuration(color, music):
    import json
    with open('./assets/data/config.json', 'w') as f:
        if color == 1:
            color = "YELLOW"
        elif color == 2:
            color = "CYAN"
        elif color == 3:
            color = "RED"

        data = (color, "game_background"+str(music))
        json.dump(data, f)
