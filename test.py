from tkinter import ttk, Tk

root = Tk()
root.geometry("900x900")

def createRect():
    s = ttk.Style()

    s.configure("rect", background="green")

    rect = ttk.Frame(root, style="rect", width=100, height=210)

    rect.pack()


createRect()
# navbar = Frame(root, bg="green", width=100)
# navbar.pack(anchor=E, fill=Y, expand=False, side= RIGHT)

# content_frame = Frame(root, bg="orange")
# content_frame.pack(anchor=W ,fill=BOTH, expand=True)



root.mainloop()
