# Connect 4 programming assignment
People in charged:

Group | Name
------ | -----
Graphical User Interface | Keanu, Pupubird
Rules, winning-state checking | Ke Xin, Wen Li
AI | Yuen Yuee

<h2 style="color:red;">component.py</h2>
it consist of:
* [Rectangle class](#For-Rectangle-class)
* [LoadingAnimation class](#For-LoadingAnimation-class)

### For Rectangle class : <a name="For-Rectangle-class"></a>

initialize it with:

    Rectangle(
        window,
        name)
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

### For LoadingAnimation class : <a name="For-LoadingAnimation-class"></a>

initialize it with:

    LoadingAnimation(window)
call *draw_loading(args)* to draw the loading animation

args of draw_loading is by following:

    draw_loading(
        y coordinate,
        x coordinate
    )

when using loading animation:

    set the daemon of the thread of loading animation to True
   
<h2 style="color:red;">game_board.py</h2>
it consists of:
* GameBoard class

### For GameBoard class :

initialize it with:

    GameBoard(
        window
    )

call *draw_board(args)* to draw the game board

args of draw_board is by following:

    draw_board(
        row_amount,
        column_amount
    )

To access game board list:

    list = instance.game_board_list

    To modify content:
    list[index].content = "<new_value>"
##### game_board_list is a one dimentional list, it contains instances of the Rectangle class.




