import json
import curses
import time
import winsound
import threading


def main(window):
    threading.Thread(target=back).start()

    for i in range(100):
        threading.Thread(target=click).start()
        time.sleep(2)


def back():
    winsound.PlaySound('assets/music/background.wav', winsound.SND_ASYNC)


def click():
    winsound.PlaySound('assets/music/clicking.wav', winsound.SND_ASYNC)


curses.wrapper(main)
