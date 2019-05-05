import os
import time
import GUI.test as test
import curses
import threading

    
def install():
    #using this curses library instead because built-in curses has import problems.
    os.system('pip install curses-2.2+utf8-cp37-cp37m-win_amd64.whl')
    print('checking update...')

def main(window):
    install()

    test.main(window)


curses.wrapper(main)