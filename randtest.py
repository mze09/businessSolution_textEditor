from tkinter import *
from tkmacosx import Button
import random

root = Tk()
root.title("Updating Labels")
root.geometry("375x175")
#label update define
def update1():
	label1.config(text="Updated 1!")
def update2():
	label2.config(text="Updated 2!")
def update3():
	label3.config(text="Updated 3!")

#literally just a copy n paste of the label update functions
def randupdate1():
	label1.config(text="Selected 1!")
def randupdate2():
	label2.config(text="Selected 2!")
def randupdate3():
	label3.config(text="Selected 3!")

#button update define
def butupdate1():
	button1.config(text="Selected 1!")
def butupdate2():
	button2.config(text="Selected 2!")
def butupdate3():
	button3.config(text="Selected 3!")

def randupdate():
	#this is a pretty lengthy script but its pretty simple in practice
	#run two different rand operations
	button = random.randint(1,3)
	if(button == 1):
		butupdate1()
	if(button == 2):
		butupdate2()
	if(button == 3):
		butupdate3()
	label = random.randint(1,3)
	#gotta make a whole new def list just for different text
	if(label == 1):
		randupdate1()
	if(label == 2):
		randupdate2()
	if(label == 3):
		randupdate3()

#defining widgets
button1 = Button(root, text="Button 1", command=update1)
button2 = Button(root, text="Button 2", command=update2)
button3 = Button(root, text="Button 3", command=update3)
randbutton = Button(root, text="Random Button", command=randupdate)
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
