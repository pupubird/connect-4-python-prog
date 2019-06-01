import curses
import json
from GUI.Component import low_level_component as component


class ScoreBoard:
    def __init__(self, window, nlines, ncols, game_mode):
        self.window = window
        self.ncols = ncols
        self.nlines = nlines
        self.game_mode = game_mode

    def draw_score_board(self):
        border = component.Rectangle(
            self.window, top_row=True, top_sym="SCORE BOARD")
        border.draw_rectangle(0, 0, self.ncols, self.nlines, False)
        self.show_scores()
        self.window.refresh()

    def show_scores(self):
        curses.init_pair(4, curses.COLOR_CYAN, 0)

        def _data_list():
            with open('./assets/data/scores.json', 'r') as f:
                data = json.load(f)
                data['scores'][self.game_mode] = sorted(
                    data['scores'][self.game_mode], key=lambda i: i[0], reverse=True)
                return data['scores'][self.game_mode]

        data = _data_list()
        try:
            j = 3
            for i in range(10):
                self.window.attron(curses.color_pair(1))
                self.window.addstr(j, 7, str(data[i][0]))
                self.window.attroff(curses.color_pair(1))

                self.window.addstr(j, 4, str(i + 1) + '.')

                self.window.addstr(j, 13, data[i][1])

                self.window.attron(curses.color_pair(4))
                self.window.addstr(j, 19, data[i][2])
                self.window.attroff(curses.color_pair(4))
                j += 3
        except IndexError:
            pass
        self.window.refresh()
