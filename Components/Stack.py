from tkinter import ttk

from Widget import Widget

class Stack(Widget):
    def __init__(self, **kwargs):
        self.savedKwargs = kwargs
    
    def setParent(self, parent):
        self.root = ttk.Frame(parent)

        super().mapKwargsToRoot(**self.savedKwargs)

        self.root.pack()