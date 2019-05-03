#For component.py:
    it consist of:
        *1.rectangle
         2.loading animation*

        _for Rectangle class_ :

            initialize it with:
                window,
                name
            call draw_rectangle(args) to draw the rectangle to the window parsed.

            args of draw_rectangle is by following:
                top left y coordinate,
                top left x coordinate,
                botton right y coordinate,
                bottom right x coordinate

            when initialize the Rectangle with content, if wanted to modify:

            <sth> = instance.content for getter
            instance.content = "<sth>" for setter
            del instance.content for delete the content (change it to " ")

        _for LoadingAnimation_ :

            initialize it with:
                window,
            call draw_loading(args) to draw the loading animation

            args of draw_loading is by following:
                y coordinate,
                x coordinate

            when using loading animation:
            
            set daemon of the waiting function to true (in threading modules)


