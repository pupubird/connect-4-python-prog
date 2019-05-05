class simulation:
    def __init__(self, init_content):
        self.show_content = init_content

    def show(self):
        print(self.show_content)

    @property
    def content(self):
        return self.show_content

    @content.setter
    def content(self, new_value):
        self.show_content = new_value


a = simulation("test1")
a.show()
a.content = "test2"
a.show()
print(a.content)
