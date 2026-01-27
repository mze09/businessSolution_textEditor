from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Reading & Writing Files")
root.geometry("450x150")

def writeFile():
	with open("demofile.txt", "w") as f:
		text = textbox.get("1.0", "end")
		f.write(text)
		

def readFile():
	with open("demofile.txt", "r") as f:
		content = f.read()
		print(content)

def openFile():
	with open("demofile.txt", "r") as f:
		content = f.read()
		textbox.insert(END, content)
	pass

textbox = Text(root, width=40, height=6)
writebutton = Button(root, text="Write To File", command=writeFile)
readbutton = Button(root, text="Read From File", command=readFile)
openbutton = Button(root, text="Open File", command=openFile)

textbox.grid(row=1, column=1, columnspan=3)
writebutton.grid(row=2, column=1)
openbutton.grid(row=2, column=2)
readbutton.grid(row=2, column=3)

root.mainloop()