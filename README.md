# Connect 4 programming assignment
People in charged:

Group | Name
------ | -----
Graphical User Interface | Keanu, Pupubird
Rules, winning-state checking | Ke Xin, Wen Li
AI | Yuen Yuee

***

## component.py
it consist of:
* [Rectangle class](#For-Rectangle-class)
* [LoadingAnimation class](#For-LoadingAnimation-class)

#### For Rectangle class : <a name="For-Rectangle-class"></a>

initialize it with:

    Rectangle(
        window,
        name
    )

    optional args for Rectangle:
    (
        top_row = False, 
        col_index = 0, 
        init_content = " "
    )

call *draw_rectangle(args)* to draw the rectangle to the window parsed.

args of draw_rectangle is by following:

    draw_rectangle(
        top left y coordinate,
        top left x coordinate,
        botton right y coordinate,
        bottom right x coordinate
    )

To modify content (e.g.: "O","X"," ") in rectangle:

    change: instance.content = new_content
    get: instance.content
    delete: del instance.content

#### For LoadingAnimation class : <a name="For-LoadingAnimation-class"></a>

initialize it with:

    LoadingAnimation(
        window
    )
call *draw_loading(args)* to draw the loading animation

args of draw_loading is by following:

    draw_loading(
        y coordinate,
        x coordinate
    )

when using loading animation:

    set the daemon of the thread of loading animation to True
   
***
## game_board.py
it consists of:
* GameBoard class

#### For GameBoard class :

initialize it with:

    GameBoard(
        window,
        box_size
    )

call *draw_board(args)* to draw the game board

args of draw_board is by following:

    draw_board(
        row_amount,
        column_amount
    )

To access game board list:

    list = instance.game_list

    To modify content:
    list[index].content = "<new_value>"

To refresh the board(after update the board data):

    instance.refresh_board()

To get the content inside all the board data:

    instance.data()

*data()* function return a two-dimensional list and automatically filled with the content of the Rectangle class.
data() takes only no argument, it returns only the content in the rectangles.

##### NOTE: game_board_list is an one dimentional list, it contains instances of the Rectangle class.




