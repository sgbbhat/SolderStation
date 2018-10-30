from tkinter import *
from tkinter import messagebox
import time
import RPi.GPIO as GPIO

cancelPressed = True

def setcancelPressed():	
	global cancelPressed
	cancelPressed = False

def Info_Messagebox(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):	
	top = Toplevel()
	top.title("Waiting for user input...")
	msg = Message(top, text = "Load Board, Then press Finger Switch")
	msg.pack()
	
	buttonCancel = Button(top, text = "Cancel", command = setcancelPressed)
	buttonCancel.pack()
	
	root.update()

	while(not GPIO.input(14)):
		time.sleep(0.1)
	
	if cancelPressed == False:
		top.destroy()
		return False
	else:
		top.destroy()
		return True
