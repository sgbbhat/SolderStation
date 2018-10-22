#!/usr/bin/env python3

# Import general modules
import datetime
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox 
from collections import OrderedDict

# Import Database Modules showDialogButton
from DatabaseQuery.database_connect import database_connect
from DatabaseQuery.execute_query_SELECT import execute_query_SELECT

# Import from Settings Modules 
from Settings.readmodel import readModel
from Settings.readINI import readINI

# Import Test Modules 
from Tests.Enter_Mfg_ID import Enter_Mfg_ID
from Tests.Verify_PN import Verify_PN
from Tests.Process_Enforcement import Process_Enforcement
from Tests.BAT1_Voltage import BAT1_Voltage
from Tests.BAT2_Voltage import BAT2_Voltage
from Tests.RST1_Voltage import RST1_Voltage
from Tests.RST2_Voltage import RST2_Voltage
from Tests.Wakeup_Pulse import Wakeup_Pulse
from Tests.Serial_Number import Serial_Number
from Tests.Test_Time import Test_Time
from Tests.Log_Test_Data_SQL import Log_Test_Data_SQL
from Tests.switcher import Select_Test

# Import Graphics Module
from Graphics.createLabel import CreateLabel

modelFileContent = OrderedDict()

def showDialogButton():
	global modelFileContent
	folder_path = filedialog.askopenfilename(initialdir = ModelDirectory , title = "Select Model File", filetypes = (("text files", "*.txt") , ("all files", "*.*")))
	FilePathLabel.config(anchor = 'w', text = folder_path)
	modelFilepath = FilePathLabel.cget("text")
	modelFileContent = readModel(modelFilepath)

root = Tk()

# Read INI file
StationName, ErrorLog, ModelDirectory = readINI()

# Error Log
ErrorLogHandle = open(ErrorLog, "a")

# Window settings
root.title(StationName)
root.geometry("650x400")
root.resizable(0,0)
root.configure(background='SlateGray4')

# Label to diplay model file heading
FilePathLabelTitle = CreateLabel(root, "FilePathLabelTitle",  "Model"  , 1,  12, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 18, 7)

# Entry widget heading
MfgIDLabelTitle = CreateLabel(root, "MfgIDLabelTitle",  "Mfg. ID"  , 1,  12, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 18, 75)

# Label to diplay Messages heading
MessagesLabelTitle = CreateLabel(root, "MessagesLabelTitle",  "Messages"  , 1,  12, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 18, 125)

# Messages Label heading
LastScannedLabelTitle = CreateLabel(root, "LastScannedLabelTitle",  "Last Scanned Mfg. ID"  , 1,  20, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 217, 75)

# Messages Label heading
LastScannedSerialNumberTitle = CreateLabel(root, "LastScannedSerialNumberTitle",  "Serial Number"  , 1,  25, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 416, 75)

# WasMfg Connection heading
WasMfgConnectionTitle = CreateLabel(root, "WasMfgConnectionTitle",  "WasMfg"  , 1,  8, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 543, 7)

# Select model file Button 
SelectModelButtonImage = PhotoImage(file = 'SelectFile.png')
SelectModelButtonImageSub = SelectModelButtonImage.subsample(18,18)
SelectModelButton = Button(root, image=SelectModelButtonImageSub, bg = 'white', command = showDialogButton)
SelectModelButton.place(x=510, y=30)

# Entry widget
mfgIdInput = Entry(root, bd = '2' , relief = "sunken")
mfgIdInput.place(x=20, y=100)

# Connection to the database
databaseHandle = database_connect()
if databaseHandle == -99:
	WasMfgConnection = Canvas(root, height = 35, width = 35, bg = 'red' )
	ErrorLogHandle.write(str(datetime.datetime.now()) + " : " + "Failed to connect to the database\n")
else:
	WasMfgConnection = Canvas(root, height = 30, width = 30, bg = 'lime green' )
WasMfgConnection.place(x=548, y=31)

# Field to diplay Serial Number
MessageDisplaySlNo = Label(root, text = "" , height = 1, width = 20, borderwidth = 3, relief = "sunken", justify = LEFT)
MessageDisplaySlNo.place(x=415, y=99)

# Field to diplay  Mfg ID 
MessageDisplayMfgID = Label(root, text = "" , height = 1, width = 20, borderwidth = 3, relief = "sunken", justify = LEFT)
MessageDisplayMfgID.place(x=217, y=99)

# Label to diplay model file name and location
FilePathLabel = Label(root, text = "" , height = 2, width = 60, borderwidth = 2, relief = "sunken")
FilePathLabel.place(x=20, y=30)

# Field to diplay Messages 
MessagesLabel = Label(root, text = "" , height = 15, width = 70, borderwidth = 1, relief = "sunken")
MessagesLabel.place(x=19, y=150)

# Main program begins
def startTest(mfgID):
	mfgID = Last_ScannedMfgID(mfgIdInput, MessageDisplayMfgID)
	Sln = Serial_Number(databaseHandle, mfgID, MessageDisplaySlNo)
	global modelFileContent
	if(bool(modelFileContent) == False):
		messagebox.showerror("Error" , "Model file not selected")

# Binding ENTER key event
root.bind('<Return>', startTest)

root.mainloop()

