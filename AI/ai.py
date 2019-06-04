def ai():
    import Rules.rules as rules
    check_list = [(3, 'X'), (3, 'O'), (2, 'X'), (1, 'X')]
    mode_list = ['hori', 'verti', 'pdiag', 'ndiag']
    for connect, sym in check_list:
        for mode in mode_list:
            value, _, boo = rules.winning_check(
                connect, 'temp_board_data', '6:7', True, mode, sym)
            if boo:
                col, row = value
                import GUI.Game_Logic.game_logic as logic
                log = logic.GameLogic()
                board_data, _, _ = log.load_saved_data('6:7')
                slot_boo, index = log.slot_check(board_data, col, True)
                if slot_boo and index == row:
                    return col, row
    return 4, -1
