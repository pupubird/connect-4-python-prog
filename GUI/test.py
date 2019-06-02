import curses


def main(window):

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    key_int = [x for x in range(97, len(alpha)+98)]
    while True:
        key = window.getch()
        if key in key_int:
            window.addstr(str(alpha[key_int.index(key)]))


curses.wrapper(main)
