# Bat_voltage
from tkinter import END
from os import *
import time 
import RPi.GPIO as GPIO

def setupGPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(14, GPIO.IN)
	GPIO.add_event_detect(14, GPIO.BOTH)
	
	while(not GPIO.input(14)):
		time.sleep(0.1)		
	GPIO.cleanup()

def BAT1_Voltage(key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	setupGPIO()
	rawScale = popen('megaio 0 aread 1').read()
	measurement = float(rawScale)/4095.0 * 3.3
	if measurement > float(val[1]) and measurement < float(val[2]) :
		result = 'Pass'
	else:
		result = 'Fail'

	# Display Test Name
	TestNameText.insert(END, "\n")
	TestNameText.insert(END, key)

	# Display Min Limit
	MinLimitText.insert(END, "\n")
	MinLimitText.insert(END, str(val[1]))

	# Display Max Limit
	MaxLimitText.insert(END, "\n")
	MaxLimitText.insert(END, str(val[2]))
	
	# Display Measurement
	MeasurementText.insert(END, "\n")
	MeasurementText.insert(END, round(measurement, 2))

	# Display Result
	ResultText.insert(END, "\n")
	ResultText.insert(END, result)

	
