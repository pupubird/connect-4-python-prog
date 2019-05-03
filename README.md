# Connect 4 programming assignment
## Component.py
#### it consist of:

    1.rectangle
    2.loading animation

### for Rectangle class :

initialize it with:

    Rectangle(window,name)
call **draw_rectangle(args)** to draw the rectangle to the window parsed.

args of draw_rectangle is by following:

    draw_rectangle(
        top left y coordinate,
        top left x coordinate,
        botton right y coordinate,
        bottom right x coordinate
    )

#### To modify content (e.g.: "O","X"," ") in rectangle:

    change: instance.content = new_content
    get: instance.content
    delete: del instance.content

###for LoadingAnimation class :

initialize it with:

    window
call **draw_loading(args)** to draw the loading animation

args of draw_loading is by following:

    draw_loading(
        y coordinate,
        x coordinate
    )

#### when using loading animation:

    set daemon of the waiting function to true (in threading modules)


