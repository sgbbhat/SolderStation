# RST_Voltage
from tkinter import END
from os import *
import time 
import re

def RST2_Voltage_Low(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	rawScale = popen('megaio 0 aread 4').read()
	measurement = float(rawScale)/4095.0 * 3.3
	
	if measurement > float(val[1]) and measurement < float(val[2]) :
		result = 'Pass'
	else:
		result = 'Fail'

	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display Test Name
	TestNameText.insert(END, "\n")
	TestNameText.insert(END, mod_TestName)

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

	if result == "Fail":
		return False
	else:
		return True
