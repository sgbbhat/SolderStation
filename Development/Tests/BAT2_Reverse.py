# Function to measure battery voltage and display test 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 

def BAT2_Reverse(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	measurement = popen('megaio 0 optread 7').read()

	# Substitues space before every capital letter
	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Decide result based on the measurement
	result = 'Pass' if float(measurement) == float(val[1]) else 'Fail'

	# Display Test and results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, float(measurement), result)
	
	if int(measurement) == 1 :
            messagebox.showerror("Error", "Battery 2 connected in Reverse")

	# Return test results
	if int(measurement) == 1 :
		return False
	else:
		return True

