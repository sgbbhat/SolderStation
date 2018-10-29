#!/usr/bin/env python3

# Import general modules
import time
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox 
from collections import OrderedDict
from tkinter import END, LEFT, BOTH

# Import Database Modules showDialogButton
from DatabaseQuery.database_connect import database_connect
from DatabaseQuery.execute_query_SELECT import execute_query_SELECT

# Import from Settings Modules 
from Settings.readmodel import readModel
from Settings.readINI import readINI

# Import Graphics Module
from Graphics.createLabel import CreateLabel

# Import Test Modules 
from Tests.Last_ScannedMfgID import Last_ScannedMfgID
from Tests.Verify_PN import Verify_PN
from Tests.Process_Enforcement import Process_Enforcement
from Tests.BAT1_Voltage import BAT1_Voltage
from Tests.BAT2_Voltage import BAT2_Voltage
from Tests.RST1_Voltage_Low import RST1_Voltage_Low
from Tests.RST2_Voltage_Low import RST2_Voltage_Low
from Tests.RST1_Voltage_High import RST1_Voltage_High
from Tests.RST2_Voltage_High import RST2_Voltage_High
from Tests.Wakeup_Pulse import Wakeup_Pulse
from Tests.Serial_Number import Serial_Number
from Tests.Test_Time import Test_Time
from Tests.Log_Test_Data_SQL import Log_Test_Data_SQL
from Tests.Get_Serial_Number import getSerialNumber
from Tests.defaultfun import defaultfun

def Select_Test(name):
	return {
		"VerifyPN" : Verify_PN, 
		"ProcessEnforcement" : Process_Enforcement,
		"BAT1Voltage" : BAT1_Voltage,
		"BAT2Voltage" : BAT2_Voltage,
		"RST1VoltageLow" : RST1_Voltage_Low,
		"RST2VoltageLow" : RST2_Voltage_Low,
		"RST1VoltageHigh" : RST1_Voltage_High,
		"RST2VoltageHigh" : RST2_Voltage_High,
		"WakeupPulse" : Wakeup_Pulse,
		"SerialNumber" : Serial_Number, 
		"TestTime" : Test_Time, 
		"LogTestData_SQL" : Log_Test_Data_SQL,
		}.get(name, defaultfun)

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

# Field to diplay TestName 
TestNameText = Text(root, height = 15, width = 40, bd = 1, relief = "sunken", bg = 'gray78')
TestNameText.insert(INSERT, "Name" )
TestNameText.place(x=19, y=150)

# Field to diplay MinLimitText 
MinLimitText = Text(root, height = 15, width = 8, bd = 1, relief = "sunken", bg = 'gray78')
MinLimitText.insert(INSERT, "Min Spec" )
MinLimitText.place(x=300, y=150)

# Field to diplay MaxLimitText
MaxLimitText = Text(root, height = 15, width = 8, bd = 1, relief = "sunken", bg = 'gray78')
MaxLimitText.insert(INSERT, "Max Spec" )
MaxLimitText.place(x=360, y=150)

# Field to diplay MeasurementText
MeasurementText = Text(root, height = 15, width = 12, bd = 1, relief = "sunken", bg = 'gray78')
MeasurementText.insert(INSERT, "Measurement" )
MeasurementText.place(x=420, y=150)

# Field to diplay ResultText
ResultText = Text(root, height = 15, width = 10, bd = 1, relief = "sunken", bg = 'gray78')
ResultText.insert(INSERT, "Result" )
ResultText.place(x=505, y=150)

# Main program begins
def startTest(mfgID):
	testStartTime = time.time()
	mfgID = Last_ScannedMfgID(mfgIdInput, MessageDisplayMfgID, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText)
	Sln = getSerialNumber(databaseHandle, mfgID, MessageDisplaySlNo)
	global modelFileContent
	if(bool(modelFileContent) == False):
		messagebox.showerror("Error" , "Model file not selected")
	for key, val in modelFileContent.items():
		if key == "" or bool(val) == False or key == 'name':
			pass
		else:
			Select_Test(key)(key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime)

# Binding ENTER key event
root.bind('<Return>', startTest)

root.mainloop()

