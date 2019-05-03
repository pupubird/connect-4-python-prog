import curses
import time
import component

#### not done yet, do not design based on this python file! ###

board_x = 10
board_y = 5
row_height = 5
row_size = 6
col_width = 10
col_size = 9

"""
example of an board list:

[[rectangle at 1x1, rectangle at 2x1, rectangle at 3x1...],
 [rectangle at 1x1...],
 [..],
 ...]

index of board list = index of row
index of row(list inside board list) = index of col

every item in board list is an instance of component.Rectangle class

e.g.: 
board[1][2] = row 2, col 3
"""


def main(window):
    # for each row, the y coordinate is decide by i * the row_height
    board = list()
    for i in range(row_size):
        row = col(window,
                  row_height * i, board_x,
                  row_height * (i + 1), col_width + board_x,
                  col_size)
        board.append(row)

    window.refresh()
    time.sleep(10)
    print(board)


def col(window, up_left_y, up_left_x, low_right_y, low_right_x, col):
    # print rectangle for each column
    current_row_list = list()
    for current_col in range(col):
        current_rectangle = component.Rectangle(window, "gameboard box")
        current_rectangle.draw_rectangle(
            board_y + up_left_y,
            (col_width * current_col)+up_left_x,
            board_y + low_right_y,
            (col_width * (current_col + 1))+up_left_x
        )
        current_row_list.append(current_rectangle)
    return current_row_list


curses.wrapper(main)
