class GameLogic:
    def slot_check(self, game_list, col_key):
        for i in range(1, len(game_list[col_key])+1):
            if game_list[col_key][-i].content == ' ':
                # if empty slot is found, return the True and the index
                return True, -i
        else:
            return False, 1

    def dropping_animation(self, board, game_list, col_key, move_index, char):
        import time
        for i in range(-6, move_index):
            game_list[
                col_key][i].content = char
            board.refresh_board()
            time.sleep(0.2)
            game_list[
                col_key][i].content = " "

        game_list[
            col_key][move_index].content = char
