
    # connected = 1

    # # check for vertical column
    # for column in board_data:
    #     # if last symbol = current row symbol, means they are the same, connect+1
    #     for current in column:
    #         if current == previous and current != " ":
    #             connected += 1
    #         else:
    #             connected = 1
    #         previous = current
    #         if connected == win_connect and previous != " ":
    #             return previous, True

    # previous = str()
    # connected = 1

    # # check for horizontal row
    # #[0][-1] [1][-1] [2][-1]
    # for i in range(1, len(board_data[0])+1):
    #     for j in range(len(board_data)):
    #         if board_data[j][-i] == previous and previous != " ":
    #             connected += 1
    #         else:
    #             connected = 1
    #         previous = board_data[j][-i]
    #         if connected == win_connect and previous != " ":
    #             return previous, True

    # previous = str()
    # connected = 1

    # previous = str()
    # connected = 1
    # # check for positive diagonal
    # for i in range(len(board_data[0])):
    #     for col in range(len(board_data)):
    #         row = 1
    #         while row <= (win_connect):
    #             try:
    #                 # col + row -1 is because whenever row + 1, col also grow with it

    #                 # [0][-1] [1][-2] [2][-3] [3][-4]
    #                 # is the same as [0][-1]==[-1][-2]==[-2][-3]==[-3][-4]...
    #                 if board_data[col + row - 1][-(row+i)] == previous and board_data[col + row - 1][-(row+i)] != ' ':
    #                     connected += 1
    #                 else:
    #                     connected = 1
    #                     previous = board_data[col + row - 1][-(row + i)]

    #                 if connected == win_connect and previous != ' ':
    #                     return previous, True
    #             except IndexError:
    #                 pass
    #             row += 1