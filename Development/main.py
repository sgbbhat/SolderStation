#!/usr/bin/env python3

# Import general modules
import datetime
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox 

# Import Database Modules 
from DatabaseQuery.database_connect import database_connect
from DatabaseQuery.execute_query_SELECT import execute_query_SELECT
from Settings.readINI import readINI

# Import Test Modules 
from Tests.Enter_Mfg_ID import Enter_Mfg_ID
from Tests.Serial_Number import Serial_Number

def showDialogButton():
	folder_path = filedialog.askopenfilename(initialdir = ModelDirectory , title = "Select Model File", filetypes = (("text files", "*.txt") , ("all files", "*.*")))
	FilePathLabel.config(anchor = 'w', text = folder_path)
	
root = Tk()

# Read INI file
StationName, ErrorLog, ModelDirectory = readINI()

# Error Log
ErrorLogHandle = open(ErrorLog, "a")

# Window settings
root.title(StationName)
root.geometry("700x400")
root.resizable(0,0)
root.configure(background='SlateGray4')

# Label to diplay model file name and location
FilePathLabel = Label(root, text = "" , height = 2, width = 60, borderwidth = 2, relief = "sunken")
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
mfgIdInput = Entry(root, bd = '2' , relief = "sunken")
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
	ErrorLogHandle.write(str(datetime.datetime.now()) + " : " + "Failed to connect to the database\n")
else:
	WasMfgConnection = Canvas(root, height = 35, width = 35, bg = 'lime green' )
WasMfgConnection.place(x=595, y=100)

# Field to diplay Messages
MessageDisplay = Label(root, text = "" , height = 1, width = 47, borderwidth = 2, relief = "sunken", justify = LEFT)
MessageDisplay.place(x=250, y=250)

# Messages Label heading
FilePathLabelTitle = Label(root, text = "Messages" , height = 1,  width = 8, relief = "flat", bg='SlateGray4', fg= 'white', font = ('Times', 11, 'bold'))
FilePathLabelTitle.place(x=252, y=225)

# Main program begins
def startTest(mfgID):
	# Insert Switcher here
	mfgID = Enter_Mfg_ID(mfgIdInput, MessageDisplay)
	Sln = Serial_Number(databaseHandle, mfgID)
	print(Sln)

# Binding ENTER key event
root.bind('<Return>', startTest)

root.mainloop()

