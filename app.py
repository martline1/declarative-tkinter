from Components.Button import Button
from Components.MainWindow import MainWindow

class App:
    def __init__(self) -> None:
        self.build()

    def build(self):
        MainWindow(
            title="Tkinter App!",
            dimensions=(600, 600),
            children=[
                Stack(
                    children= [
                        Button(
                            text="Click me!",
                            onClick= lambda: print("Hello world!")
                        ),
                        Positioned(
                            child= Button(
                                text="Positioned Button!",
                                onClick= lambda: print("Click on positioned button"),
                            ),
                        ),
                    ],
                ),
            ],
        )
