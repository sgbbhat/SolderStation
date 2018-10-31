from tkinter import *
from tkinter import messagebox
import time
import RPi.GPIO as GPIO

cancelPressed = True

def setcancelPressed():	
	global cancelPressed
	cancelPressed = False

def Info_Messagebox_Before(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):		
	global cancelPressed	
	cancelPressed = True
	GPIO.add_event_detect(14, GPIO.RISING, bouncetime = 1000)		
	top = Toplevel(master = root)
	top.geometry("%dx%d%+d%+d" % (200, 150,750,450))
	top.title("Waiting for user input...")
	msg = Message(top, text = "Load Board, Then Press Finger Switch To Start", width = 200)
	msg.place(x=0,y=0)

	buttonCancel = Button(top, text = "Cancel", command = setcancelPressed)
	buttonCancel.place(x=50,y=70)
	
	top.attributes('-topmost', 'true')	
	
	root.update()

	while(not GPIO.input(14)):
		continue
	
	GPIO.remove_event_detect(14)

	time.sleep(1)
	if cancelPressed == False:
		top.destroy()
		return False
	else:
		top.destroy()
		return True
