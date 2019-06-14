# Connect 4
###### 2019 March Programming Principle Assignment 2, group 4

Introduction and selling point here

Task | Person in charged
----|----
GUI | Chang Cheng, Keanu
Rules| Ke Xin, Wen Li
AI| Yuen Yuee


## Getting Started

Double click the app.py in order to launh the program

## Classes and function in program

Class|Function|Function description|Value Returned| Parameters|Parameter Description
---|---|---|---|---|---
Rectangle|__init\__()|initialize the rectangle class|NA|window,  init_content*, top_row*, top_sym*, color*| * = optional, Rectangle will be created on the **window** parsed, **init_content** is the content that will be at the middle of the rectangle (i.e. "start"), **top_row** is a boolean parameter (True = there are string that will be displayed at the top of the rectangle (i.e. +---1---+), **top_sym** is a string parameter for top_row (i.e. 1/Score Board/X), **color** is the color of the content, use curses defined color for this parameter (i.e. curses.COLOR_YELLOW)
 . |draw_rectangle()|draw rectangle at the y and x given,it get the top left corner position,and bottom right corner position to draw the rectangle on the window initialized|NA|up_left_y, up_left_x, low_right_y, low_right_x,default_corn_sym = True| **up_left_y** is the top left corner's y value, **up_left_x** is the top left corner's x value, and same to **low_right_y** and **low_right x**
 .| property function: content, color| functions that with @property, so that it can be changed in future, content is the content that is in the rectangle, color is the color of the content|-|-|-
 LoadingAnimation|__init\__()|initialize the loading animation class| NA| window|-
 .|draw_loading()|draw the loading animation at the y and x given| NA|y,x|-
 GameBoard|__init\__()|initialize the board|NA|window,box_size|box_size is the size for every tile in the board
 .|draw_board()|draw the game board at the window parsed with the row and column that required (i.e. 6,7 or 6,9)| NA| row_amount,column_amount| -
 .|data()|return the data of the board in a two-dimensional list| two-dimensional list in syntax of [column][row]|-|-
 .|data_reset()|it cleasr every data inside the game board list to empty string|NA|-|-
 



## Layer of abstraction in program
![Screenshot](https://raw.githubusercontent.com/pupubird/connect-4-python-prog/master/abstraction.PNG)
Figure above shown layers of abstraction in the program, Everything is based on a Rectangle class which is a class that draw a rectangle. Rectangle class will be the based class for every board tile, every button, and the score board.


### Issues

Please do remind that the window scaling must be 125% and below.
If you are facing a issue like '_curses_error addwstr() returned ERR', it means the scale of the window is above 125%, to solve, please follow the steps bellow:

1. open Setting
2. click System
3. choose 'Display' tab
4. Search for 'Scale and Layout'
5. change the scale to 125% and below



## Built With

* [Curses](https://docs.python.org/2/library/curses.html) - The UI framework





