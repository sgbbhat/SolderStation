
from tkinter import filedialog
from tkinter import *

def readFile(name):
	

def showDialogButton():
	global folder_path
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select files", filetypes = (("jpeg files","*.jpeg") , ("all files", "*.*")))
	fileContent = readFile(filename)
	folder_path.set(fileContent)

root = Tk()
folder_path = StringVar()
button2 = Button(text = "Browse", command = showDialogButton)
button2.grid(row=0, column=3)
print(getglobal())
root.mainloop()
