import os
import time
import threading
import subprocess


def main():
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

    # adjust window size
    win_width, _ = get_widheight()
    if int(win_width) > 1900:
        os.system('mode 200')
    else:
        os.system('mode 150')


def get_widheight():
    os.system('wmic desktopmonitor get screenheight, screenwidth > a.txt')
    with open("a.txt", 'r') as f:
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


main()
