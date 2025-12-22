from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Text Editor")

root.geometry("600x200")

label1 = Label(root, text="Company 1")
label2 = Label(root, text="- Notes 1 [ Lorem ipsum d... ]")
searchbox = Text(root, width=60, height=2)

searchbox.grid(row=1, column=0)
label1.grid(row=2, column=0)
label2.grid(row=3, column=0)
label1.config(font=("Arial", 25))

root.mainloop()