import os
try:
    import curses
except Exception:
    # means it might be the first time the user run the program
    try:
        os.system('pip install "curses-2.2+utf8-cp37-cp37m-win_amd64.whl"')
    except Exception:
        # user is using 32-bit python
        os.system('pip install "curses-2.2+utf8-cp37-cp37m-win32.whl"')
    # open terminal to run the program as shell doesnt run it well
    os.system('start cmd.exe @cmd /k "python app.py"')
import time


def main(window):  # adjust window size
    import GUI.game_board_page as board_page
    # start background music
    import threading
    background_music = threading.Thread(target=music, daemon=True)
    background_music.start()
    curses.curs_set(0)
    os.system('mode 165')
    # direct to board page
    board_page.main(window, 6, 9)


def music():
    import winsound
    winsound.PlaySound('assets/music/background.wav', winsound.SND_LOOP)


curses.wrapper(main)
