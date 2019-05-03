import curses
import component


class _BoardColumn:
    def __init__(self, window, row_size, box_size, game_board_list=[]):
        self.window = window
        self.row_size = row_size
        self.box_size = box_size
        self.game_board_list = game_board_list

    def draw_column(self, up_left_y, up_left_x, low_right_y, low_right_x):
        for row in range(self.row_size):
            current_row = component.Rectangle(self.window)
            current_row.draw_rectangle(
                up_left_y + (self.box_size * row),
                up_left_x,
                low_right_y + (self.box_size*row),
                low_right_x + self.box_size
            )
            self.game_board_list.append(current_row)

    @property
    def game_list(self):
        return self.game_board_list


class GameBoard(_BoardColumn):
    def __init__(self, window, game_board_list='', row_size='', box_size=''):
        super().__init__(game_board_list, row_size, box_size)
        self.window = window

    def draw_board(self, row_amount, column_amount):
        box_size = 5
        for column in range(0, column_amount * 2, 2):
            # jump by two to avoid overlay
            board = _BoardColumn(self.window,
                                 column_amount,
                                 box_size)
            board.draw_column(0,
                              box_size * column,
                              box_size,
                              box_size * (column + 1))
        self.window.refresh()


if __name__ == "__main__":
    import time

    def main(window):
        # print board
        demo = GameBoard(window)
        demo.draw_board(6, 9)
        time.sleep(2)
        # to access to board box content
        game_list = demo.game_board_list
        # change content
        game_list[1].content = "O"
        print(game_list[1].content)

    curses.wrapper(main)
