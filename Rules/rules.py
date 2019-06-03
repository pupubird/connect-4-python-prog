import json


def load_data(filename, game_mode):
    # read json file here, return a two dimemsional list
    with open(f'./assets/data/{filename}.json', 'r') as f:
        board_data = json.load(f)
    return board_data['board_data'][game_mode]


def winning_check(win_connect, filename, game_mode):
    board_data = load_data(filename, game_mode)

    previous = str()
    connected = 1

    # check for vertical column
    for column in board_data:
        # if last symbol = current row symbol, means they are the same, connect+1
        for current in column:
            if current == previous and current != " ":
                connected += 1
            else:
                connected = 1
            previous = current
            if connected == win_connect and previous != " ":
                return previous, True
        # reset for every column
        previous = str()
        connected = 1

    previous = str()
    connected = 1

    # check for horizontal row
    #[0][-1] [1][-1] [2][-1]
    for i in range(1, len(board_data[0])+1):
        for j in range(len(board_data)):
            if board_data[j][-i] == previous and previous != " ":
                connected += 1
            else:
                connected = 1
            previous = board_data[j][-i]
            if connected == win_connect and previous != " ":
                return previous, True
        # reset for every row
        previous = str()
        connected = 1

    previous = str()
    connected = 1
    # check for positive diagonal
    for i in range(len(board_data[0])):
        for col in range(len(board_data)):
            row = 1
            while row <= (win_connect):
                try:
                    # col + row -1 is because whenever row + 1, col also grow with it

                    # [0][-1] [1][-2] [2][-3] [3][-4]
                    if board_data[col + row - 1][-(row+i)] == previous and board_data[col + row - 1][-(row+i)] != ' ':
                        connected += 1
                    else:
                        connected = 1
                        previous = board_data[col + row - 1][-(row + i)]

                    if connected == win_connect and previous != ' ':
                        return previous, True
                except IndexError:
                    pass
                row += 1

    previous = str()
    connected = 1
    # check for negative diagonal
    for i in range(len(board_data[0])):
        for col in range(len(board_data)-win_connect+1):
            row = 1
            while row <= (win_connect):
                try:
                    # col + row -1 is because whenever row + 1, col also grow with it
                    # [-1][-1] [-2][-2] -> [-1][-2] [-2][-3]
                    if board_data[-(row)][-(row+i)] == previous and board_data[-(row)][-(row+i)] != ' ':
                        connected += 1
                    else:
                        connected = 1
                        previous = board_data[-(row)][-(row + i)]
                    if connected == win_connect and previous != ' ':
                        return previous, True
                except IndexError:
                    pass
                row += 1

    # check for draw
    for column in board_data:
        for row in column:
            if row == " ":
                break
        else:
            continue
        break  # only execute when inner loop does break
    else:
        return "draw", True  # all filled, draw

    return "none", False


# win_connect = 4 when 6X7 gameboard is chosen
# win_connect = 5 when 6X9 gameboard is chosen
if __name__ == "__main__":
    value, boo = winning_check(5)
    print(value)
