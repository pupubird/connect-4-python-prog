import json


def load_data(filename, game_mode):
    # read json file here, return a two dimemsional list
    with open(f'./assets/data/{filename}.json', 'r') as f:
        board_data = json.load(f)
    return board_data[filename][game_mode]


def winning_check(win_connect, filename, game_mode):
    board_data = load_data(filename, game_mode)

    # initialize previous and connect_col
    previous_c = str()
    connect_col = 1

    # check for vertical column
    for column in board_data:
        # if last symbol = current row symbol, means they are the same, connect+1
        for current in column:
            if current == previous_c and current != " ":
                connect_col += 1
            else:
                previous_c = current
                connect_col = 1
            if connect_col == win_connect and previous_c != " ":
                return previous_c, True

    # initialize connect_row
    previous_r = str()
    connect_row = 1
    # check for horizontal row
    #[0][-1] [1][-1] [2][-1]
    for i in range(1, len(board_data[0])+1):
        for j in range(len(board_data)):
            if board_data[j][-i] == previous_r and previous_r != " ":
                connect_row += 1
            else:
                previous_r = board_data[j][-i]
                connect_row = 1
            if connect_row == win_connect and previous_r != " ":
                return previous_r, True

    # initialize connect_pdiag and previous
    previous_pd = str()
    connect_pdiag = 1

    # check for positive diagonal
    for col in range(len(board_data)):
        row = 1
        while row <= (win_connect+1):
            try:
                # col + row -1 is because whenever row + 1, col also grow with it
                # is the same as [0][-1]==[-1][-2]==[-2][-3]==[-3][-4]...
                if board_data[col + row - 1][-(row)] == previous_pd and board_data[col + row - 1][-(row)] != ' ':
                    connect_pdiag += 1
                else:
                    connect_pdiag = 1
                previous_pd = board_data[col + row - 1][-(row)]

                if connect_pdiag == win_connect and previous_pd != ' ':
                    return previous_pd, True
            except IndexError:
                pass
            row += 1

    # initialize connect_ndiag and previous
    previous_nd = str()
    connect_ndiag = 1

    # check for negative diagonal from bottom right

    for col in range(len(board_data)):
        row = 1
        while row <= (win_connect+1):
            try:
                if board_data[-(col + row)][-(row)] == previous_nd and board_data[-(col + row)][-(row)] != ' ':
                    connect_ndiag += 1
                else:
                    connect_ndiag = 1
                previous_nd = board_data[-(col + row)][-(row)]

                if connect_ndiag == win_connect and previous_nd != ' ':
                    return previous_nd, True
            except IndexError:
                pass
            row += 1

    return "none", False


# win_connect = 4 when 6X7 gameboard is chosen
# win_connect = 5 when 6X9 gameboard is chosen
if __name__ == "__main__":
    value, boo = winning_check(5)
    print(value)
