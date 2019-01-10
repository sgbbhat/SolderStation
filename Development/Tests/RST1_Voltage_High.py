# Test to measure Reset voltage when the reset is released 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult

# Function returs True if the rest voltage is within the limits when set to high, else returns false
def RST1_Voltage_High(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	rawScale = popen('megaio 0 aread 3').read()
	measurement = float(rawScale)/4095.0 * 3.3 
	
	# Decide result based on the measurement
	result = 'Pass' if measurement > float(val[1]) and measurement < float(val[2])  else 'Fail'

	# Substitues space before every capital letter
	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display test and results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)

	# Return test result
	if result == "Fail":
		return False
	else:
		return True
