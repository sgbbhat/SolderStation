from tkinter import *
from tkinter import messagebox
import time
import RPi.GPIO as GPIO

cancelPressed = True

def setcancelPressed():	
	global cancelPressed
	cancelPressed = False
	messagebox.showerror("Error", "Testing Aborted")
	pass

def Info_Messagebox_After(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):		
	global cancelPressed
	cancelPressed = True	
	GPIO.add_event_detect(14, GPIO.FALLING, bouncetime = 1000)		
	top = Toplevel(master = root)
	top.geometry("%dx%d%+d%+d" % (200, 170,750,450))
	top.title("Waiting for user input...")
	top.resizable(0,0)

	msg = Message(top, text = "Press Finger Switch When Solder Is Complete To Check Assembly\n \n CLAMP MUST BE DOWN", width = 200)
	msg.place(x=10,y=10)

	buttonCancel = Button(top, text = "Cancel", command = setcancelPressed)
	buttonCancel.place(x=50,y=100)
	
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
