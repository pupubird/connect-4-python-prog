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
    win_width, _ = get_widheight()
    if int(win_width) > 1700:
        os.system('mode 200')
    else:
        os.system('mode 150')
    board_page.main(window, int(win_width))


def get_widheight():
    os.system('wmic desktopmonitor get screenheight, screenwidth > scrn_size.txt')
    with open("scrn_size.txt", 'r') as f:
        lines = f.readlines()

    # because of unable to strip()
    size_line = lines[2]
    height_line = size_line[0:9]
    width_line = size_line[29:36]

    height = ""
    width = ""
    for height_int in height_line:
        try:
            height += str(int(height_int))
        except Exception:
            pass

    for width_int in width_line:
        try:
            width += str(int(width_int))
        except Exception:
            pass

    return width, height


curses.wrapper(main)
