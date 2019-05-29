import json


def data_import(filename):
    #read json file here, return a two dimemsional list

def winning_check(win_connect):
    #board_data = data_import(filename)
    board_data = [
        [' ', ' ', ' ', ' ', ' ', 'O'],
        [' ', ' ', 'O', 'O', 'O', 'O'],
        [' ', ' ', 'X', 'O', 'X', 'X'],
        [' ', ' ', 'O', 'X', 'O', 'O'],
        [' ', 'X', 'O', 'O', 'X', 'O'],
        [' ', ' ', 'X', 'O', 'O', 'X'],
        [' ', ' ', ' ', 'X', 'O', 'O'],
        [' ', ' ', ' ', 'X', 'X', 'X'],
        [' ', ' ', ' ', ' ', 'X', 'X']
    ]



    # initialize previous and connect_col
    previous_c = str()
    connect_col = 1

    #check for vertical column
    for column in board_data:
        # if last symbol = current row symbol, means they are the same, connect+1
        for current in column:
            if current == previous_c and current != " ":
                connect_col += 1
            else:
                previous_c = current
                connect_col = 1
        if connect_col == win_connect and previous_c != " ":
            return True
    # initialize connect_row
    previous_r = str()
    connect_row = 1
    #check for horizontal row
    for row in board_data:
        for current in row:
            if current == previous_r and current != " ":
                connect_row += 1
            else:
                previous_r = current
                connect_row = 1
        if connect_row == win_connect and previous_r != " ":
            return True

    #initialize connect_pdiag and previous
    previous_pd = str()
    connect_pdiag = 1

    #check for positive diagonal
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
                    return True
            except IndexError:
                pass
            row += 1

    #initialize connect_ndiag and previous
    previous_nd = str()
    connect_ndiag = 1

    #check for negative diagonal from bottom right

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

                    return True
            except IndexError:
                pass
            row += 1
    return False



# win_connect = 4 when 6X7 gameboard is chosen
# win_connect = 5 when 6X9 gameboard is chosen
print(winning_check(3))


win = winning_check(5)



