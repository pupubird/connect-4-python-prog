# save scores and show sapnu here
import curses


class GameOverPage:
    # width:100, height:40
    def __init__(self, window, orig_window, status, total_attempt, game_mode):
        self.window = window
        self.orig_window = orig_window
        self.status = status
        self.total_attempt = total_attempt
        self.game_mode = game_mode
        self.main()

    def main(self):

        import threading
        if self.status == "O":
            text = "win"
        elif self.status == "X":
            text = "lose"
        elif self.status == "draw":
            text = "draw"
        threading.Thread(target=self.play_background,
                         args=[text], daemon=True).start()

        # draw status
        curses.init_pair(1, curses.COLOR_YELLOW, 0)
        self.window.attron(curses.color_pair(1))
        with open(f"./assets/ASCII_Art/{text}.txt", "r") as logo:
            text = logo.readlines()
            for row in range(1, len(text)+1):
                self.window.addstr(row+3, 35, text[row-1])
        self.window.refresh()
        self.window.attroff(curses.color_pair(1))

        # print total attempt
        if self.total_attempt > 15:
            string = "You can do better"
        elif self.total_attempt >= 10 and self.total_attempt <= 15:
            string = "Not too bad"
        elif self.total_attempt < 10:
            string = "You have the talent!"
        self.window.addstr(
            8+3, 36, f"Your total attempt: {self.total_attempt}")
        self.window.addstr(9 + 3, 36, string)

        # score
        size = self.game_mode.split(":")
        hori_size = size[0]
        verti_size = size[1]
        if self.status == "O":
            score = ((int(hori_size) * int(verti_size)) -
                     self.total_attempt) * 100
        elif self.status == "X":
            score = self.total_attempt * 100
        self.window.addstr(11+3, 36, f"Your score: {score}")

        self.window.border()
        self.window.refresh()

        import GUI.Component.low_level_component as rectangle

        name = rectangle.Rectangle(
            self.window, top_row=True, top_sym="Your Name(Only alphabet)")
        name.draw_rectangle(18, 25, 22, 68)

        # player name input
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        key_int = [x for x in range(97, len(alpha)+98)]
        while True:
            key = self.window.getch()
            if key in key_int:
                name.content += str(alpha[key_int.index(key)])
                name.refresh_rectangle()
            if key == curses.KEY_ENTER or key in [10, 13]:
                self.save_score(name.content, score)
                import app
                app.main(self.orig_window)
                break
            self.window.refresh()

        self.window.refresh()
        self.distrup_music()

    def play_background(self, state):
        import winsound
        winsound.PlaySound(
            f'./assets/music/{state}.wav', winsound.SND_LOOP | winsound.SND_ASYNC)

    def distrup_music(self):
        import winsound
        winsound.PlaySound(
            None, winsound.SND_PURGE
        )

    def save_score(self, name, score):
        import json
        score_data = dict()
        with open('./assets/data/scores.json', 'r') as f:
            score_data = json.load(f)
        with open('./assets/data/scores.json', 'w') as f:
            from datetime import date
            today = date.today()
            data = [score, name, today.strftime("%d/%m/%Y")]
            score_data['scores'][self.game_mode].append(data)

            json.dump(score_data, f)
            import GUI.Game_Logic.game_logic as log
            logic = log.GameLogic()
            logic.reset_data(self.game_mode)
