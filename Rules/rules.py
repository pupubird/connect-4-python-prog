import json


def load_data(filename, game_mode):
    # read json file here, return a two dimemsional list
    with open(f'./assets/data/{filename}.json', 'r') as f:
        board_data = json.load(f)
    return board_data['board_data'][game_mode]


def winning_check(win_connect, filename, game_mode, ai_mode=False, specific_check="", specific_sym=""):
    board_data = load_data(filename, game_mode)
    '''
    This checking method is a blindfold checking,
    we only look for the last symbol and the current symbol,

    if current symbol = last symbol, means they are consecutively connected, 
    hence the counter += 1

    by doing this, we can avoid hardcoding and be able to reused again by the AI -> ai.py
    for pattern checking
    '''

    def verti_check():
        previous = str()
        connected = 1
        # vertical check
        for i in range(len(board_data)):
            for j in range(1, len(board_data[i])+1):
                if board_data[i][-j] == previous and previous != " ":
                    connected += 1
                else:
                    connected = 1
                previous = board_data[i][-j]
                if connected == win_connect and previous != " ":
                    if ai_mode:
                        if board_data[i][-j] == specific_sym:
                            try:
                                if board_data[i][-(j + 1)] == " ":
                                    return (i, -(j+1)), "verti", True
                            except Exception:
                                pass
                        return (0, 0), "", False
                    else:
                        return board_data[i][-j], "", True
            previous = str()
            connected = 1
        # nothing found
        return (0, 0), "verti", False

    def hori_check():
        previous = str()
        connected = 1
        # horizontal check
        for i in range(1, len(board_data[0])+1):
            for j in range(len(board_data)):
                if board_data[j][-i] == previous and previous != " ":
                    connected += 1
                else:
                    connected = 1
                previous = board_data[j][-i]
                if connected == win_connect and previous != " ":
                    if ai_mode:
                        if board_data[j][-i] == specific_sym:
                            try:  # check for the right hand side of the connected row
                                if board_data[j+1][-i] == " ":
                                    return (j + 1, -i), "hori", True
                            except Exception:
                                pass
                            try:  # check for left hand side of the connected row
                                if board_data[j - win_connect][-i] == " " and j - 1 != -1:
                                    return (j - win_connect, -i), "hori", True
                            except Exception:
                                pass
                    else:
                        return board_data[j][-i], "", True
            # reset for every row
            previous = str()
            connected = 1

        return (0, 0), "hori", False

    def pdiag_check():
        previous = str()
        connected = 1
        # check for positive diagonal
        for i in range(len(board_data[0])):
            for col in range(len(board_data)):
                row = 1
                while row <= (win_connect):
                    try:
                        if board_data[col + row - 1][-(row+i)] == previous and board_data[col + row - 1][-(row+i)] != ' ':
                            connected += 1
                        else:
                            connected = 1
                            previous = board_data[col + row - 1][-(row + i)]

                        if connected == win_connect and previous != ' ':

                            if ai_mode:
                                if board_data[col + row - 1][-(row + i)] == specific_sym:
                                    try:  # check for right hand side of the connected positive diagonal
                                        if board_data[col + row][-(row + i + 1)] == " ":
                                            return (col + row, -(row + i + 1)), "pdiag", True
                                    except Exception:
                                        pass
                                    try:  # check for left hand side
                                        if board_data[col + row - 1 - win_connect][-(row + i - win_connect)] == " ":
                                            return (col + row - 1 - win_connect, (-(row + i - win_connect))), "pdiag", True
                                    except Exception:
                                        pass
                                return (0, 0), "", False
                            else:
                                return board_data[col + row - 1][-(row+i)], "", True

                    except IndexError:
                        pass
                    row += 1

                previous = str()
                connected = 1

        return (0, 0), "pdiag", False

    def ndiag_check():
        previous = str()
        connected = 1
        # check for negative diagonal
        for i in range(len(board_data[0])):
            for col in range(len(board_data)-win_connect+1):
                row = 1
                while row <= len(board_data):
                    try:
                        if board_data[-(row+col)][-(row+i)] == previous and board_data[-(row+col)][-(row+i)] != ' ':
                            connected += 1
                        else:
                            connected = 1
                            previous = board_data[-(row + col)][-(row + i)]
                        if connected == win_connect and previous != ' ':
                            if ai_mode:
                                if board_data[-(row+col)][-(row + i)] == specific_sym:
                                    try:  # right hand side
                                        if board_data[-(row + col + 1)][-(row + i + 1)] == " ":
                                            return (-(row + col+1), -(row + i + 1)), "ndiag", True
                                    except Exception:
                                        pass

                                    try:  # left hand side
                                        if board_data[-(row + col - win_connect)][-(row + i - 1)] == " ":
                                            return (-(row + col - win_connect), -(row + i - 1)), "ndiag", True
                                    except Exception:
                                        pass

                            else:
                                return board_data[-(row+col)][-(row + i)], "", True
                    except IndexError:
                        pass
                    row += 1
                previous = str()
                connected = 1

        return (0, 0), "ndiag", False

    if ai_mode:  # AI mode on, check for specific pattern
        if specific_check == "pdiag":
            value, mode, boo = pdiag_check()
            if boo:
                return value, mode, boo
        elif specific_check == "ndiag":
            value, mode, boo = ndiag_check()
            if boo:
                return value, mode, boo
        elif specific_check == "verti":
            value, mode, boo = verti_check()
            if boo:
                return value, mode, boo
        elif specific_check == "hori":
            value, mode, boo = hori_check()
            if boo:
                return value, mode, boo
    else:
        value, mode, hori_boo = hori_check()
        if hori_boo:
            return value, mode, hori_boo
        value, mode, verti_boo = verti_check()
        if verti_boo:
            return value, mode, verti_boo
        value, mode, pdiag_boo = pdiag_check()
        if pdiag_boo:
            return value, mode, pdiag_boo
        value, mode, ndiag_boo = ndiag_check()
        if ndiag_boo:
            return value, mode, ndiag_boo
            # check for draw
        for column in board_data:
            for row in column:
                if row == " ":
                    break
            else:
                continue
            break  # only execute when inner loop does break
        else:
            return "draw", "", True  # all filled, draw
    return (0, 0), "", False


# win_connect = 4 when 6X7 gameboard is chosen
# win_connect = 5 when 6X9 gameboard is chosen
if __name__ == "__main__":
    value, boo = winning_check(5)
    print(value)
