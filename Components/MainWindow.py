from tkinter import Tk

from Components.Widget import Widget

class MainWindow(Widget):
    def __init__(self, **kwargs):
        self.root = Tk()

        super().__init__(**kwargs)

        self.root.mainloop()
