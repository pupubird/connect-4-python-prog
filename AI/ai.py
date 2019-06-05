def ai(game_mode):
    import Rules.rules as rules
    import GUI.Game_Logic.game_logic as logic
    log = logic.GameLogic()
    board_data, _, _ = log.load_saved_data(game_mode)

    data = game_mode.split(':')
    if int(data[1]) == 9:
        check_list = [(4, 'X'), (4, 'O'), (3, 'X'), (2, 'X'), (1, 'X')]
    else:
        check_list = [(3, 'X'), (3, 'O'), (2, 'X'), (1, 'X')]

    mode_list = ['hori', 'verti', 'pdiag', 'ndiag']

    for connect, sym in check_list:
        for mode in mode_list:
            value, _, boo = rules.winning_check(
                connect, 'temp_board_data', game_mode, True, mode, sym)
            if boo:
                col, row = value
                slot_boo, index = log.slot_check(board_data, col, True)
                if slot_boo and index == row:
                    return col, row
    # means no move available, most likely to be the first move
    import random
    rand_col = random.choice([x for x in range(int(data[1]))])
    rand_boo, index = log.slot_check(board_data, rand_col, True)
    if rand_boo:
        return rand_col, index
    while not rand_boo:
        rand_col = random.choice([x for x in range(int(data[1]))])
        rand_boo, index = log.slot_check(board_data, rand_col, True)
        if rand_boo:
            return rand_col, index
