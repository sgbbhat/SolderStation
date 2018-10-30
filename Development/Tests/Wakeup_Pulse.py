# Wakeup_Pulse
from tkinter import END
import re

def Wakeup_Pulse(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	result = "Pass"
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
	MeasurementText.insert(END, 1)

	# Display Result
	ResultText.insert(END, "\n")
	ResultText.insert(END, result)

	if result == "Fail":
		return False
	else:
		return True
