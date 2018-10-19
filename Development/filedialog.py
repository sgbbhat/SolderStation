
from tkinter import filedialog
from tkinter import *

folder_path = ""

def showDialogButton():
	global folder_path
	folder_path = filedialog.askopenfilename(initialdir = "/", title = "Select files", filetypes = (("text files", "*.txt") , ("all files", "*.*")))
	FilePathLabel.config(text = folder_path)

root = Tk()

# Window settings
root.title("Solder Station")
root.geometry("700x400")
root.resizable(0,0)
root.configure(background='SlateGray4')

# Label to diplay model file name and location
FilePathLabel = Label(root, text = "" , height = 3, width = 60, borderwidth = 4, relief = "groove")
FilePathLabel.place(x=60, y=100)

# Label to diplay model file heading
FilePathLabelTitle = Label(root, text = "Model" , height = 1,  width = 8, relief = "flat", bg='SlateGray4', fg= 'white')
FilePathLabelTitle.place(x=55, y=65)

# Select model file Button 
SelectModelButtonImage = PhotoImage(file = 'SelectFile.png')
SelectModelButtonImageSub = SelectModelButtonImage.subsample(11,11)
SelectModelButton = Button(root, image=SelectModelButtonImageSub, bg = 'white', command = showDialogButton)
SelectModelButton.place(x=550, y=100)



root.mainloop()
