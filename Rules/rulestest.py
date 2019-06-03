import json


def load_data(filename, game_mode):
    # read json file here, return a two dimemsional list
    with open(f'./assets/data/{filename}.json', 'r') as f:
        board_data = json.load(f)
    return board_data['board_data'][game_mode]


def winning_check(win_connect, filename, game_mode):
    board_data = load_data(filename, game_mode)
    board_data = [
        [
            "X",
            "X",
            "X",
            "X",
            " ",
            " "
        ],
        [
            " ",
            " ",
            " ",
            " ",
            " ",
            "X"
        ],
        [
            " ",
            " ",
            " ",
            " ",
            " ",
            " "
        ],
        [
            " ",
            " ",
            " ",
            " ",
            " ",
            " "
        ],
        [
            " ",
            " ",
            " ",
            " ",
            " ",
            " "
        ],
        [
            " ",
            " ",
            " ",
            " ",
            " ",
            " "
        ],
        [
            " ",
            " ",
            " ",
            " ",
            " ",
            " "
        ]
    ]

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


if __name__ == "__main__":
    print(winning_check(4, 'temp_board_data', '6:7'))
