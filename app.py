import os
import time
import threading
import subprocess
import GUI.game_board_page as board_page

try:
    import GUI.test as test
    import curses
except Exception:
    try:
        # using this curses library instead because built-in curses has import problems.
        os.system('pip install "curses-2.2+utf8-cp37-cp37m-win_amd64.whl"')
    except Exception:
        # user is using 32 bit python
        os.system('pip install "curses-2.2+utf8-cp37-cp37m-win32"')


def main(window):  # adjust window size
    curses.curs_set(0)
    os.system('mode 170')
    # direct to board page
    board_page.main(window, 6, 9)


curses.wrapper(main)
