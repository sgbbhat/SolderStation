# Function to measure battery voltage and display test 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 

def BAT2_Reverse(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	rawScale = popen('megaio 0 aread 2').read()

	# Decide result based on the measurement
	result = 'Pass' if int(rawScale) > 100 else 'Fail'

	# Substitues space before every capital letter
	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display Test and results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, float(measurement), result)

	# Return test results
	if int(rawScale) < 100 :
		messagebox.showerror("Error", "Battery 2 connected in Reverse")
		return False
	else:
		return True

