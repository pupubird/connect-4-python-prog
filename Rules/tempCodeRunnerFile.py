try:
                    # col + row -1 is because whenever row + 1, col also grow with it

                    #[0][-1] [1][-2] [2][-3] [3][-4]
                    # is the same as [0][-1]==[-1][-2]==[-2][-3]==[-3][-4]...
                    if board_data[col + row - 1][-(row+i)] == previous and board_data[col + row - 1][-(row+i)] != ' ':
                        connected += 1
                    else:
                        connected = 1
                    previous = board_data[col + row - 1][row]

                    if connected == win_connect and previous != ' ':
                        return previous, True
                except IndexError:
                    pass
                row += 1