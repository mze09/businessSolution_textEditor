from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Reading & Writing Files")
root.geometry("300x150")

def writeFile():
	with open("demofile.txt", "w") as f:
		f.write("this is what will be inside of the file!")
def readFile():
	pass

textbox = Text(root, width=30, height=4)
writebutton = Button(root, text="Write To File", command=writeFile)
readbutton = Button(root, text="Read From File", command=readFile)

textbox.grid(row=1, column=1)
writebutton.grid(row=2, column=1)
readbutton.grid(row=3, column=1)

root.mainloop()