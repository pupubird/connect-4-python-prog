class GameLogic:
    def slot_check(self, game_list, col_key):
        for i in range(1, len(game_list[col_key])+1):
            if game_list[col_key][-i].content == ' ':
                # if empty slot is found, return the True and the index
                return True, -i
        else:
            return False, 1
