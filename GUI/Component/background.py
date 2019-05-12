import curses
import random
import sys
import time


snowflakes = {
    '♦': 1,
    '┼': 0.8,
    '·': 0.4,
}


def max_dimensions(window):
    height, width = window.getmaxyx()
    return height - 2, width - 1


def snowflake_char(window):
    width = max_dimensions(window)[1]
    char = random.choice(list(snowflakes.keys()))
    position = random.randrange(1, width)
    return (0, position, char)


def update_snowflakes(prev, window):
    window.attrset(curses.color_pair(1))
    new = {}
    for (height, position), char in prev.items():
        max_height = max_dimensions(window)[0]
        new_height = height
        if random.random() <= snowflakes[char]:
            new_height += 1
            if new_height > max_height or prev.get((new_height, position)):
                new_height -= 1
        new[(new_height, position)] = char
    return new


def redisplay(snowflakes, window):
    window.attrset(curses.color_pair(1))
    for (height, position), char in snowflakes.items():
        max_height, max_width = max_dimensions(window)
        if height > max_height or position >= max_width:
            continue
        window.addch(height, position, char)


def main(window, speed):
    curses.init_pair(1, curses.COLOR_YELLOW, 0)
    curses.curs_set(0)

    snowflakes = {}
    while True:
        height, width = max_dimensions(window)
        if len(snowflakes.keys()) >= 0.95 * (height * width):
            snowflakes.clear()
        snowflakes = update_snowflakes(snowflakes, window)
        snowflake = snowflake_char(window)
        snowflakes[(snowflake[0], snowflake[1])] = snowflake[2]
        window.clear()
        redisplay(snowflakes, window)
        window.refresh()
        try:
            time.sleep((0.2) / (speed / 100))
        except ZeroDivisionError:
            time.sleep(0.2)
