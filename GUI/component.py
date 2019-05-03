import curses
import time
import threading


class Rectangle:

    def __init__(self, window, top_row=False, col_index=0, init_content=" "):
        self.window = window
        self.box_content = init_content
        self.top_row = top_row
        self.col_index = col_index

    def draw_rectangle(self, up_left_y, up_left_x, low_right_y, low_right_x):
        vertical_line = curses.ACS_VLINE
        horizontal_line = "-"
        corner_symb = "+"
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
            self.window.addch(up_left_y, up_left_x, corner_symb)
            self.window.addch(up_left_y, low_right_x, corner_symb)
            self.window.addch(low_right_y, low_right_x, corner_symb)
            self.window.addch(low_right_y, up_left_x, corner_symb)

            if self.top_row:
                self.window.addstr(
                    up_left_y,
                    up_left_x + ((low_right_x - up_left_x) // 2),
                    str(self.col_index)
                )
        except Exception:
            return False
        return True

    @property
    def content(self):
        return self.box_content

    @content.setter
    def content(self, new_content):
        self.box_content = new_content

    @content.deleter
    def content(self, del_content):
        self.box_content = " "


class LoadingAnimation:
    def __init__(self, window):
        self.window = window

    def draw_loading(self, y, x):
        animation_frame = ['-', '\\', '|', '/']
        current_frame = 0
        while True:
            self.window.addstr(y, x, animation_frame[current_frame])
            if current_frame == len(animation_frame) - 1:
                current_frame = 0
            else:
                current_frame += 1
            self.window.refresh()
            time.sleep(0.5)


if __name__ == "__main__":
    def main(window):
        threadRunning = threading.Thread(target=another_function)
        animation = threading.Thread(target=test, args=[window], daemon=True)

        animation.start()
        threadRunning.start()

    def test(window):
        test_ani = LoadingAnimation(window)
        test_ani.draw_loading(0, 0)

    def another_function():
        time.sleep(3)

    curses.wrapper(main)
