from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Updating Labels")
root.geometry("400x200")

#defining widgets
button1 = Button(root, text="Button 1")
button2 = Button(root, text="Button 2")
button3 = Button(root, text="Button 3")
randbutton = Button(root, text="Random Button")
label1 = Label(root, text="Label 1")
label2 = Label(root, text="Label 2")
label3 = Label(root, text="Label 3")

#placing all widgets
button1.grid(row=1, column=1)
button2.grid(row=2, column=1)
button3.grid(row=3, column=1)
label1.grid(row=1, column=4)
label2.grid(row=2, column=4)
label3.grid(row=3, column=4)
randbutton.grid(row=4, column=2, columnspan=2)

label1.config(font=("Arial", 15))
label2.config(font=("Arial", 15))
label3.config(font=("Arial", 15))
button1.config(font=("Arial", 15))
button2.config(font=("Arial", 15))
button3.config(font=("Arial", 15))
randbutton.config(font=("Arial", 15))

root.mainloop()
