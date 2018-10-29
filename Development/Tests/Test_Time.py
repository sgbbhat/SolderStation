import time
from tkinter import END

def Test_Time(key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	endTime = time.time()

	measurement = int(endTime - testStartTime)
	if measurement >= int(val[1]) and measurement <= int(val[2]):
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
	MeasurementText.insert(END, measurement)

	# Display Result
	ResultText.insert(END, "\n")
	ResultText.insert(END, result)
