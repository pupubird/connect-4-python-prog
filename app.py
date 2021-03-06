
import os
import time

try:
    import curses
except Exception:
    # means it might be the first time the user run the program
    print("installing update...")
    print("Please hold on...")
    try:
        os.system('pip install "curses-2.2+utf8-cp37-cp37m-win_amd64.whl"')
    except Exception:
        # user is using 32-bit python
        os.system('pip install "curses-2.2+utf8-cp37-cp37m-win32.whl"')
    # open terminal to run the program as shell doesnt run it well
    while True:
        os.system('start cmd.exe @cmd /k "python app.py"')
        break
    else:
        input("""if you are facing any issue:
                1. make sure python is in the system path
                2. make sure the window is maximized
            press any key to continue..."""
              )
        os.system('start cmd.exe @cmd /k "python app.py"')


def main(window):
    import GUI.game_board_page as board_page
    import GUI.main_menu as main_menu

    # start background music
    import threading
    background_music = threading.Thread(target=music, daemon=True)

    # resize the window
    curses.resize_term(49, 165)

    # direct to menu page
    background_music.start()
    curses.curs_set(0)
    try:
        main_menu.main(window)
    except Exception:
        input("""If you are facing a 'addwstr() returned ERR' problem,
        1. go to search bar, type scale, click the 'make everything bigger' button and adjust the scale to 125%""")


def music():
    import winsound
    winsound.PlaySound('assets/music/menu_background.wav',
                       winsound.SND_LOOP | winsound.SND_ASYNC)


if __name__ == "__main__":
    curses.wrapper(main)
