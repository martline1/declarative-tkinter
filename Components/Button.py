import tkinter

from Components.Widget import Widget

class Button(Widget):
    def __init__(self, **kwargs):
        self.savedKwargs = kwargs

    def setParent(self, parent):
        self.root = tkinter.Button(parent)

        super().mapKwargsToRoot(**self.savedKwargs)

        self.root.pack()
