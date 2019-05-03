import curses
import component


class _BoardColumn:
    def __init__(self, window, row_size, box_size, game_board_list=[]):
        self.window = window
        self.row_size = row_size
        self.box_size = box_size
        self.game_board_list = game_board_list

    def draw_column(self, up_left_y, up_left_x, low_right_y, low_right_x, col_index):
        for row in range(self.row_size):
            if not row:
                current_row = component.Rectangle(
                    self.window, top_row=True, col_index=col_index)
                current_row.draw_rectangle(
                    up_left_y + (self.box_size * row),
                    up_left_x,
                    low_right_y + (self.box_size*row),
                    low_right_x + self.box_size
                )
                self.game_board_list.append(current_row)
            else:
                current_row = component.Rectangle(
                    self.window)
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
    # inherit the game board list from _BoardColumn and pass row size to _BoardColumn
    def __init__(self, window, box_size, row_size, game_board_list=''):
        super().__init__(game_board_list, row_size, box_size)

        self.window = window
        self.box_size = box_size

    def draw_board(self, row_amount, column_amount):
        for column in range(0, column_amount * 2, 2):
            # jump by two to avoid overlay
            board = _BoardColumn(self.window,
                                 column_amount,
                                 self.box_size)
            board.draw_column(0,
                              self.box_size * column,
                              self.box_size,
                              self.box_size * (column + 1),
                              (column//2)+1)
        self.window.refresh()


if __name__ == "__main__":
    import time

    def main(window):
        # print board
        demo = GameBoard(window, 3, 6)
        demo.draw_board(6, 9)
        time.sleep(10)

        # to access to board box content
        game_list = demo.game_list

        # change content
        game_list[1].content = "O"
        print(game_list[1].content)

        # to sort the list
        new_list = []
        for i in range(1, 7):
            col_list = []
            for j in range(9):
                col_list.append(game_list[0])
                game_list.pop(0)
            new_list.append(col_list)

    curses.wrapper(main)
