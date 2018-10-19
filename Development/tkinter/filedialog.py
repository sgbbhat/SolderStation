
from tkinter import filedialog
from tkinter import *

folder_path = ""

def showDialogButton():
	global folder_path
	folder_path = filedialog.askopenfilename(initialdir = "/", title = "Select files", filetypes = (("text files", "*.txt") , ("all files", "*.*")))
	FilePathLabel.config(text = folder_path)

root = Tk()

# Select model file Button 
SelectModelButtonImage = PhotoImage(file = 'SelectFile.png')
SelectModelButtonImageSub = SelectModelButtonImage.subsample(6,6)
SelectModelButton = Button(root, image=SelectModelButtonImageSub, bg = 'white', command = showDialogButton)
SelectModelButton.grid(row=0, column=30)
FilePathLabel = Label(root, text = "" , height = 3, width = 60, borderwidth = 4, relief = "groove")
FilePathLabel.grid(row=0, column=0)
root.mainloop()
