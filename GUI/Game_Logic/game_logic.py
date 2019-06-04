class GameLogic:
    def slot_check(self, game_list, col_key, ai_mode=False):
        for i in range(1, len(game_list[col_key]) + 1):
            if ai_mode:
                if game_list[col_key][-i] == ' ':
                    # if empty slot is found, return True and the index
                    return True, -i
            else:
                if game_list[col_key][-i].content == ' ':
                    # if empty slot is found, return True and the index
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
            board.refresh_board()

        game_list[
            col_key][move_index].content = char
        board.refresh_board()

    def save_data(self, content_list, game_mode, total_attempt):
        import json
        file = f"./assets/data/temp_board_data.json"
        with open(file, 'r') as f:
            data = json.load(f)
            with open(file, 'w') as g:
                # read first, then replace
                data['board_data'][game_mode] = content_list
                data['meta'][game_mode]['total_attempt'] = total_attempt
                data['meta'][game_mode]['exists'] = 1
                json.dump(data, g, indent=2)

    def load_saved_data(self, game_mode):
        import json
        with open('./assets/data/temp_board_data.json', 'r') as f:
            data = json.load(f)
            return data['board_data'][game_mode], data['meta'][game_mode]['total_attempt'], data['meta'][game_mode]['exists']

    def reset_data(self, game_mode):
        import json

        try:
            with open('./assets/data/temp_board_data.json', 'r') as f:
                data = json.load(f)
                with open('./assets/data/temp_board_data.json', 'w') as g:
                    mode = game_mode.split(':')
                    row = mode[0]
                    col = mode[1]
                    data_list = []
                    for i in range(int(col)):
                        current_list = []
                        for j in range(int(row)):
                            current_list.append(" ")
                        data_list.append(current_list)

                    data['board_data'][game_mode] = data_list
                    data['meta'][game_mode]['exists'] = 0
                    data['meta'][game_mode]['total_attempt'] = 0

                    json.dump(data, g, indent=2)
        except Exception:
            with open('./assets/data/temp_board_data.json', 'w') as f:
                data = {
                    "meta": {
                        "6:9": {
                            "exists": 0,
                            "total_attempt": 0
                        },
                        "6:7": {
                            "exists": 0,
                            "total_attempt": 0
                        }
                    },
                    "board_data": {
                        "6:9": [],
                        "6:7": []
                    }
                }
                json.dump(data, f, indent=2)

            with open('./assets/data/temp_board_data.json', 'w') as g:
                mode = game_mode.split(':')
                row = mode[0]
                col = mode[1]
                data_list = []
                for i in range(int(col)):
                    current_list = []
                    for j in range(int(row)):
                        current_list.append(" ")
                    data_list.append(current_list)

                data['board_data'][game_mode] = data_list

                json.dump(data, g, indent=2)
