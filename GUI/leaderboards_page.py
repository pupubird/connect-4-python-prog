import curses
import GUI.Component.score_board as score_board


class LeaderBoardsPage:
    def __init__(self, window):
        self.window = window
        self.game_mode = "6:7"
        self.main()

    def main(self):
        curses.resize_term(49, 165)
        self.window.clear()
        self.window.refresh()

        # draw the logo, set it to yellow colour
        curses.init_pair(1, curses.COLOR_YELLOW, 0)
        self.window.attron(curses.color_pair(1))
        with open("./assets/ASCII_Art/leaderboard.txt", "r") as logo:
            text = logo.readlines()
            for row in range(1, len(text)+1):
                self.window.addstr(row, 43, text[row-1])
        self.window.refresh()
        self.window.attroff(curses.color_pair(1))

        six_seven = curses.newwin(40, 70, 7, 13)
        six_nine = curses.newwin(40, 70, 7, 84)
        score_board.ScoreBoard(six_seven, 59, 34,
                               '6:7').draw_score_board('6:7')
        score_board.ScoreBoard(six_nine, 59, 34,
                               '6:9').draw_score_board('6:9')

        self.window.addstr(42, 64, "Press Enter to return to menu")
        self.window.refresh()

        key = self.window.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            import winsound
            winsound.PlaySound('./assets/music/clicking.wav',
                               winsound.SND_FILENAME)
