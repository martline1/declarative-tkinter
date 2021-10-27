# Declarative Tkinter

This project is inspired by Google's Flutter sdk for creating cross-platform applications.

**Python's Tkinter** is a procedural library for creating GUI Applications, this repo implements tkinter but exposes a more declarative-flutter like api for developers.

### Example code:
```py
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
```

## Author
Alcalá León Yael Mártin A. <yael.alcalla@gmail.com>
