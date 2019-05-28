import curses
from GUI.Component import low_level_component as component


class ScoreBoard:
    def __init__(self, window, nlines, ncols):
        self.window = window
        self.ncols = ncols
        self.nlines = nlines

    def draw_score_board(self):
        border = component.Rectangle(
            self.window, top_row=True, top_sym="Score board")
        border.draw_rectangle(0, 0, self.ncols, self.nlines, False)
        self.window.refresh()
