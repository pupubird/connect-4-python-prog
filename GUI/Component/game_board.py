import curses
import random
import GUI.Component.low_level_component as component


class _BoardColumn:
    """
    row size is the amount of row in the game
    box size is the width and the height of the box of the board's tiles

    Everytime draw_column create a Rectangle class, it is going to store it 
    into game_board_list for future access

    This class draw the boxes column by column, not row by row,
    hence it has to be careful when handling with the data
    """

    def __init__(self, window, row_size, box_size, game_board_list=[]):
        self.window = window
        self.row_size = row_size
        self.box_size = box_size
        self.game_board_list = game_board_list

    def draw_column(self, up_left_y, up_left_x, low_right_y, low_right_x, col_index):
        import json
        with open('./assets/data/config.json', 'r') as f:
            data = json.load(f)
            if data[0] == "YELLOW":
                color = curses.COLOR_YELLOW
            elif data[0] == "CYAN":
                color = curses.COLOR_CYAN
            elif data[0] == "RED":
                color = curses.COLOR_RED
            else:
                color = curses.COLOR_YELLOW

        self.args = up_left_y, up_left_x, low_right_y, low_right_x, col_index
        for row in range(self.row_size):
            if not row:
                current_row = component.Rectangle(
                    self.window, top_row=True, top_sym=col_index, color=color)
                current_row.draw_rectangle(
                    up_left_y + (self.box_size * row),
                    up_left_x,
                    low_right_y + (self.box_size*row),
                    low_right_x + self.box_size,
                )
                self.game_board_list.append(current_row)
            else:
                current_row = component.Rectangle(
                    self.window, color=color)
                current_row.draw_rectangle(
                    up_left_y + (self.box_size * row),
                    up_left_x,
                    low_right_y + (self.box_size*row),
                    low_right_x + self.box_size,
                )
                self.game_board_list.append(current_row)

    def refresh_board(self):
        for item in self.game_board_list:
            item.refresh_rectangle()
        self.window.refresh()


class GameBoard(_BoardColumn):
    # inherit the game board list from _BoardColumn and pass row size to _BoardColumn
    def __init__(self, window, box_size, row_size='', game_board_list=''):
        super().__init__(game_board_list, row_size, box_size)

        self.window = window
        self.box_size = box_size

    def draw_board(self, row_amount, column_amount):
        self.row_amount = row_amount
        self.column_amount = column_amount
        for column in range(0, column_amount * 2, 2):
            # jump by two to avoid overlay
            board = _BoardColumn(self.window,
                                 self.row_amount,
                                 self.box_size)
            board.draw_column(0,
                              self.box_size * column,
                              self.box_size,
                              self.box_size * (column + 1),
                              (column//2)+1)
        self.window.refresh()

    def data(self):
        content_list = [item.content for item in self.game_board_list]
        data = []
        for i in range(self.column_amount):
            data.append(
                content_list[i * self.row_amount: (self.row_amount) + (i * self.row_amount)])
        return data

    def data_set(self, new_data):
        set_content_list = [item for item in self.game_board_list]
        set_data = []
        for i in range(self.column_amount):
            set_data.append(
                set_content_list[i * self.row_amount: (self.row_amount) + (i * self.row_amount)])

        for i in range(len(set_data)):
            for j in range(len(set_data[i])):
                set_data[i][j].content = new_data[i][j]

    @property
    def game_list(self):
        board_list = [item for item in self.game_board_list]
        board_data = []
        for i in range(self.column_amount):
            board_data.append(
                board_list[i * self.row_amount: (self.row_amount) + (i * self.row_amount)])
        return board_data


if __name__ == "__main__":
    import time

    def main(window):
        # print board
        demo = GameBoard(window, 6)
        demo.draw_board(6, 9)
        time.sleep(2)

        # to access to board box content
        game_list = demo.game_list

        # change content
        game_list[1].content = "O"
        print("content:", game_list[1].content)

        # get data

        data_list = demo.data()
        print(data_list)

        # update board
        demo.refresh_board()
        time.sleep(3)

    curses.wrapper(main)
