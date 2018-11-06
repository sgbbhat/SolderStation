from tkinter import *
from tkinter import messagebox
import time
import RPi.GPIO as GPIO

cancelPressed = True

def setcancelPressed():
	global cancelPressed
	messagebox.showerror(title = 'Error', message = "Test Aborted")
	cancelPressed = False
	pass

def Info_Messagebox_Before(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):		
	global cancelPressed	
	cancelPressed = True
	GPIO.add_event_detect(14, GPIO.FALLING, bouncetime = 1000)		
	top = Toplevel(master = root)
	top.geometry("%dx%d%+d%+d" % (200, 130,750,450))
	top.title("Waiting for user input...")
	top.resizable(0,0)
	msg = Message(top, text = "LOAD BOARD, THEN PRESS FINGER SWITCH TO START.", width = 200)
	msg.place(x=10,y=10)

	buttonCancel = Button(top, text = "Cancel", command = setcancelPressed)
	buttonCancel.place(x=65,y=70)

	top.attributes('-topmost', 'true')	
	root.update()

	while(not GPIO.input(14) and (cancelPressed == True)):
		top.update()
		continue
	time.sleep(0.5)
	GPIO.remove_event_detect(14)
	if cancelPressed == False:
		top.destroy()
		return False
	else:
		top.destroy()
		return True
