# Connect 4 programming assignment
People in charged:

Group | Name
------ | -----
Graphical User Interface | Keanu, Pupubird
Rules, winning-state checking | Ke Xin, Wen Li
AI | Yuen Yuee

## Component.py
it consist of:
* [Rectangle class](#For-Rectangle-class)
* [LoadingAnimation class](#For-LoadingAnimation-class)

#### For Rectangle class :

initialize it with:

    Rectangle(window,name)
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

#### For LoadingAnimation class :

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


