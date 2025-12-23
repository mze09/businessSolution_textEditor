from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Text Editor")

root.geometry("600x300")

label1 = Label(root, text="Company 1")
label2 = Label(root, text="Company 2")
notes1 = Label(root, text="- Notes 1 [ Lorem ipsum d... ]", padx= -80)
notes2 = Label(root, text="- Notes 2 [ Lorem ipsum d... ]", padx= -80)
notes3 = Label(root, text="- Notes 3 [ Lorem ipsum d... ]", padx= -80)
notes4 = Label(root, text="- Notes 4 [ Lorem ipsum d... ]", padx= -80)
notes5 = Label(root, text="- Notes 5 [ Lorem ipsum d... ]", padx= -80)
notes6 = Label(root, text="- Notes 6 [ Lorem ipsum d... ]", padx= -80)
searchbox = Text(root, width=60, height=2)

searchbox.grid(row=1, column=0, columnspan=2)
label1.grid(row=2, column=0)
notes1.grid(row=3, column=1)
notes2.grid(row=4, column=1)
notes3.grid(row=5, column=1)

label2.grid(row=6, column=0)
notes4.grid(row=7, column=1)
notes5.grid(row=8, column=1)
notes6.grid(row=9, column=1)

label1.config(font=("Arial", 25))
label2.config(font=("Arial", 25))
notes1.config(font=("Arial", 15))
notes2.config(font=("Arial", 15))
notes3.config(font=("Arial", 15))
notes4.config(font=("Arial", 15))
notes5.config(font=("Arial", 15))
notes6.config(font=("Arial", 15))
root.mainloop()