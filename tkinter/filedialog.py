
from tkinter import filedialog
from tkinter import *

def showDialogButton():
	global folder_path
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select files", filetypes = (("text files", "*.txt") , ("all files", "*.*")))
	folder_path.set(filename)

root = Tk()
folder_path = StringVar()
button_pressed = BooleanVar()
button2 = Button(text = "Browse", command = showDialogButton)
button2.grid(row=0, column=3)
print(folder_path)

root.mainloop()
