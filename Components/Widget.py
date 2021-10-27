class Widget:
    def mapKwargsToRoot(self, **kwargs):
        for key, value in kwargs.items():
            if key == "dimensions":
                self.root.geometry(f"{value[0]}x{value[1]}")

            if key == "title":
                self.root.title(value)

            if key == "onClick":
                self.root.configure(command= value)

            if key == "text":
                self.root["text"] = value

            if key == "children":
                for child in value:
                    child.setParent(self.root)

    def __init__(self, **kwargs):
        self.mapKwargsToRoot(**kwargs)
