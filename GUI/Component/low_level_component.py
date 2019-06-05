import curses
import time
import threading


class Rectangle:

    def __init__(self, window, **kwargs):

        self.window = window
        try:
            self.box_content = kwargs['init_content']
        except KeyError:
            self.box_content = " "

        try:
            self.top_row = kwargs['top_row']
        except KeyError:
            self.top_row = False
        try:
            self.col_index = kwargs['top_sym']
        except KeyError:
            self.col_index = '-'
        try:
            self.content_color = kwargs['color']
        except KeyError:
            self.content_color = curses.COLOR_WHITE

    def draw_rectangle(self, up_left_y, up_left_x, low_right_y, low_right_x, default_corn_sym=True):
        self.args = (up_left_y, up_left_x, low_right_y, low_right_x)
        # corner color, border color, and content color
        curses.init_pair(1, curses.COLOR_YELLOW, 0)
        curses.init_pair(2, curses.COLOR_CYAN, 0)
        curses.init_pair(3, self.color, 0)
        curses.init_pair(4, curses.COLOR_CYAN, 0)
        # symbol
        vertical_line = curses.ACS_VLINE
        horizontal_line = "-"
        if not default_corn_sym:
            left_upcorner = curses.ACS_ULCORNER
            left_downcorner = curses.ACS_LLCORNER
            right_upcorner = curses.ACS_URCORNER
            right_downcorner = curses.ACS_LRCORNER
        else:
            left_upcorner = left_downcorner = right_upcorner = right_downcorner = "+"
        """
        Draw a rectangle with corners at the provided upper-left
        and lower-right coordinates.
        """
        try:
            # vertical line
            self.window.vline(up_left_y+1, up_left_x, vertical_line,
                              low_right_y - up_left_y - 1)
            self.window.vline(up_left_y+1, low_right_x, vertical_line,
                              low_right_y - up_left_y - 1)
            # horizontal line
            self.window.hline(up_left_y, up_left_x+1, horizontal_line,
                              low_right_x - up_left_x - 1)
            self.window.hline(low_right_y, up_left_x + 1, horizontal_line,
                              low_right_x - up_left_x - 1)

            # corner
            self.window.attron(curses.color_pair(1))
            self.window.addch(up_left_y, up_left_x, left_upcorner)
            self.window.addch(up_left_y, low_right_x, right_upcorner)
            self.window.addch(low_right_y, low_right_x, right_downcorner)
            self.window.addch(low_right_y, up_left_x, left_downcorner)
            self.window.attroff(curses.color_pair(1))

            # content
            if self.content == "X":
                self.window.addstr(
                    (low_right_y - up_left_y) // 2 + up_left_y,
                    (low_right_x - up_left_x) // 2 +
                    up_left_x - (len(self.content)//2),
                    self.content,
                    curses.color_pair(4)
                )
            else:
                self.window.addstr(
                    (low_right_y - up_left_y) // 2 + up_left_y,
                    (low_right_x - up_left_x) // 2 +
                    up_left_x - (len(self.content)//2),
                    self.content,
                    curses.color_pair(3)
                )

            # draw for top row numbers
            if self.top_row:

                self.window.attron(curses.color_pair(2))
                self.window.addstr(
                    up_left_y,
                    # align to center
                    up_left_x + ((low_right_x - up_left_x) // 2)
                    - (len(str(self.col_index))//2),
                    str(self.col_index)
                )
                self.window.attroff(curses.color_pair(2))

        except Exception:
            return False
        return True

    # redraw the rectangle without redefine the args
    def refresh_rectangle(self):
        up_left_y, up_left_x, low_right_y, low_right_x = self.args
        self.draw_rectangle(up_left_y, up_left_x, low_right_y, low_right_x)

    @property
    def content(self):
        return self.box_content

    @content.setter
    def content(self, new_content):
        self.box_content = new_content

    @content.deleter
    def content(self, del_content):
        self.box_content = " "

    @property
    def color(self):
        return self.content_color

    @color.setter
    def color(self, new_color):
        self.content_color = new_color


class LoadingAnimation:
    def __init__(self, window):
        self.window = window

    def draw_loading(self, y, x):
        import random
        animation_frame = ['-', '\\', '|', '/']
        current_frame = 0
        time_count = 0
        time_limit = random.choice([6, 5, 4, 3])
        while time_count < time_limit:
            self.window.addstr(y, x, animation_frame[current_frame])
            if current_frame == len(animation_frame) - 1:
                current_frame = 0
            else:
                current_frame += 1
            self.window.refresh()
            time.sleep(0.5)
            time_count += 1
        self.window.addstr(y, x, " ")


if __name__ == "__main__":
    def main(window):
        threadRunning = threading.Thread(target=another_function)
        animation = threading.Thread(target=test, args=[window], daemon=True)

        animation.start()
        threadRunning.start()

        rectangle = Rectangle(window)
        rectangle.draw_rectangle(0, 0, 10, 10)
        rectangle.content = "O"
        time.sleep(2)
        rectangle.refresh_rectangle()
        time.sleep(3)

    def test(window):
        test_ani = LoadingAnimation(window)
        test_ani.draw_loading(0, 0)

    def another_function():
        time.sleep(3)

    curses.wrapper(main)
