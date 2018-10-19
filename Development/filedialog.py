
from tkinter import filedialog
from tkinter import *
from database_connect import database_connect
from execute_query_SELECT import execute_query_SELECT
from tkinter import messagebox 

def showDialogButton():
	folder_path = filedialog.askopenfilename(initialdir = "/home/pi/Documents/SolderStation/Models", title = "Select Model File", filetypes = (("text files", "*.txt") , ("all files", "*.*")))
	FilePathLabel.config(text = folder_path)

root = Tk()

# Window settings
root.title("Solder Station")
root.geometry("700x400")
root.resizable(0,0)
root.configure(background='SlateGray4')

# Label to diplay model file name and location
FilePathLabel = Label(root, text = "" , height = 2, width = 60, borderwidth = 4, relief = "groove")
FilePathLabel.place(x=60, y=100)

# Label to diplay model file heading
FilePathLabelTitle = Label(root, text = "Model" , height = 1,  width = 8, relief = "flat", bg='SlateGray4', fg= 'white', font = ('Times', 11, 'bold'))
FilePathLabelTitle.place(x=51, y=77)

# Select model file Button 
SelectModelButtonImage = PhotoImage(file = 'SelectFile.png')
SelectModelButtonImageSub = SelectModelButtonImage.subsample(16,16)
SelectModelButton = Button(root, image=SelectModelButtonImageSub, bg = 'white', command = showDialogButton)
SelectModelButton.place(x=550, y=100)

# Entry widget
mfgIdInput = Entry(root, bd = '2' , relief = "groove")
mfgIdInput.place(x=60, y=250)

# Entry widget heading
FilePathLabelTitle = Label(root, text = "Mfg. ID" , height = 1,  width = 8, relief = "flat", bg='SlateGray4', fg= 'white', font = ('Times', 11, 'bold'))
FilePathLabelTitle.place(x=52, y=225)

# WasMfg Connection heading
WasMfgConnectionTitle = Label(root, text = "WasMfg" , height = 1,  width = 8, relief = "flat", bg='SlateGray4', fg= 'white', font = ('Times', 11, 'bold'))
WasMfgConnectionTitle.place(x=587, y=77)

# Connection to the database
databaseHandle = database_connect()
if databaseHandle == -99:
	WasMfgConnection = Canvas(root, height = 35, width = 35, bg = 'red' )
	print("Failed to connect to the database")
else:
	WasMfgConnection = Canvas(root, height = 35, width = 35, bg = 'lime green' )

WasMfgConnection.place(x=595, y=100)

root.mainloop()

