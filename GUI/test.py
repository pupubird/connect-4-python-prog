import curses
import threading
import time
import random
from curses import panel
from GUI import snowterm
from GUI import game_board


def main(window):
    window.border()
    window.addstr(11, 3, "wtfffffffffffffffffffffffffffff")

    window2 = curses.newwin(30, 150, 5, 7)

    window.refresh()
    window2.refresh()

    time.sleep(1)

    snow = threading.Thread(target=snowterm.main, args=[
                            window, 20], daemon=True)
    window_obj = threading.Thread(target=refreshwin, args=[window2])

    window_obj.start()
    snow.start()

    time.sleep(3)


def refreshwin(window):
    board = game_board.GameBoard(window, 5)
    board.draw_board(5, 14)

    gamelist = board.game_list

    ran = threading.Thread(target=rand, args=[board, gamelist])
    ran.start()
    while True:
        board.refresh_board()


def rand(board, gamelist):
    for item in gamelist:
        item.content = random.choice(['O', 'X', ' '])
        time.sleep(1)
        board.refresh_board()


if __name__ == "__main__":
    curses.wrapper(main)
