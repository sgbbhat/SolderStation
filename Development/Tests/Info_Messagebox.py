from tkinter import *
from tkinter import messagebox
import time
import RPi.GPIO as GPIO

cancelPressed = True

def setcancelPressed():	
	global cancelPressed
	cancelPressed = False

def Info_Messagebox(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(14, GPIO.IN)
	GPIO.add_event_detect(14, GPIO.BOTH)	
	
	top = Toplevel()
	top.title("Waiting for user input...")
	msg = Message(top, text = "Load Board, Then press Finger Switch")
	msg.pack()
	
	buttonCancel = Button(top, text = "Cancel", command = setcancelPressed)
	buttonCancel.pack()
	
	root.update()

	while((not GPIO.input(14)) or (not cancelPressed)):
		time.sleep(0.1)
	
	if cancelPressed == False:
		top.destroy()
		return False
	else:
		return True
	
	GPIO.cleanup()
