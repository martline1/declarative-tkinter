from Components.Button import Button
from Components.MainWindow import MainWindow

class App:
    def __init__(self) -> None:
        self.build()

    def build(self):
        MainWindow(
            title="Tkinter App!",
            dimensions=(300,200),
            children=[
                Button(
                    text="Click me!",
                    onClick= lambda: print("Hello world!")
                ),
                Button(
                    text="Click me!",
                    onClick= lambda: print("Hello world!")
                ),
            ],
        )
