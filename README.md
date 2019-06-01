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
        window
    )

    default optional args for Rectangle:
    (
        top_row = False, 
        col_index = '-', 
        init_content = "",
        color = curses.COLOR_WHITE
    )

call *draw_rectangle(args)* to draw the rectangle to the window parsed.

args of draw_rectangle is by following:

    draw_rectangle(
        top left y coordinate,
        top left x coordinate,
        botton right y coordinate,
        bottom right x coordinate,
        default_corn_sym = True
    )

    where default_corn_sym is True by default = "+",
    change it to False means the corner will be ACS line corner (e.g.:curses.ACS_LLCORNER)

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
    list[col][row].content = "<new_value>"

To refresh the board(after update the board data):

    instance.refresh_board()

To get the content inside all the board data:

    instance.data()

To change all the content inside board data so some list:

    instance.data_set(new_list)

*data()* function return a two-dimensional list and automatically filled with the content of the Rectangle class.
data() takes only no argument, it returns only the content in the rectangles.

##### NOTE: game_board_list is an one dimentional list, it contains instances of the Rectangle class.

####For ScoreBoard class:
initialize it with:

    ScoreBoard(
        window, 
        nlines, #width 
        ncols, #height
        game_mode
    )

To draw on window:

    draw_score_board()

    it will autimatically draw it on the 0,0 of the window parse, so create a newwin for ScoreBoard is advicable


####For board game page:

    GameBoardPage(
        window, 
        row_size, 
        col_size, 
        game_mode,
        load_saved=False
    )

