from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Text Editor")

root.geometry("800x400")

searchbox = Text(root)

searchbox.grid (row=2, column=1, columnWidth=2)

root.mainloop()