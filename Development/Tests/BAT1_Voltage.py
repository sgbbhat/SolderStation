# Function measures battery voltage
from tkinter import END
from os import *
import time
import re
from Tests.displayResult import displayResult
from tkinter import messagebox

# Function measures Battery Voltage, returns True if voltage measurement within max and min limits, else return False
def BAT1_Voltage(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	rawScale = popen('megaio 0 aread 1').read()
	measurement = float(rawScale)/4095.0 * 3.74 * 2.0

	# Substitues space before every capital letter
	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Decide result based on the measurement
	result = 'Pass' if measurement > float(val[1]) and measurement < float(val[2]) else 'Fail'

	# Display tests and results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)

	# Pop-up message in case of bad battery
	if result == 'Fail' :
            messagebox.showerror("Error", "Bad Battery 1")

	# Return test results
	if result == "Fail":
		return False
	else:
		return True
