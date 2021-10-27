# Declarative Tkinter

This project is inspired by Google's Flutter sdk for creating cross-platform applications.

**Python's Tkinter** is a procedural library for creating GUI Applications, this repo implements tkinter but exposes a more declarative-flutter like api for developers.

### Example of the resulting declarative code:
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

### Same code with pure Tkinter:
```py
from tkinter import Tk, Button

def tkApp():
    mainWindow = Tk()

    mainWindow.title("Tkinter App!")
    mainWindow.geometry("300x200")

    button1 = Button(mainWindow, text="Click me!")
    button1.config(command= lambda: print("Hello world"))
    button1.pack()

    button2 = Button(mainWindow, text="Click me!")
    button2.config(command= lambda: print("Hello world"))
    button2.pack()

    mainWindow.mainLoop()
```

## Author
Alcalá León Yael Mártin A. <yael.alcalla@gmail.com>
