import json
import curses
import time


def dataa():
    with open('./assets/data/scores.json', 'r') as f:
        data = json.load(f)
        data['scores'] = sorted(
            data['scores'], key=lambda i: i[0], reverse=True)
        return data['scores']


def main(window):
    data = dataa()
    j = 1
    for i in range(10):
        window.addstr(j, 4, str(i+1)+'.')
        window.addstr(j, 7, str(data[i][0]))
        window.addstr(j, 13, data[i][1])
        window.addstr(j, 19, data[i][2])
        j += 1
    window.refresh()
    time.sleep(3)


curses.wrapper(main)
