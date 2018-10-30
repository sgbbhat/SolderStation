#Verify_PN
from tkinter import END
import re

def Verify_PN(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	databaseHandle.execute("Select distinct ProcessFlowKey from dbo.TestEvent WHERE MfgSerialNumber = ? AND ProcessFlowKey != 0", mfgID)
	ProcessFlowKey = databaseHandle.fetchall()
	CurrentPartNumber = modelFileContent['Part_No']
	CurrentProcessStep = 'Board Test'
	databaseHandle.execute("Select PrePartNumber from dbo.ProcessEnforcementStep WHERE ProcessFlowKey = ? AND CurrentPartNumber = ? AND CurrentProcessStep = ?", int((ProcessFlowKey[0])[0]), CurrentPartNumber[0], CurrentProcessStep)
	PrePartNumber = databaseHandle.fetchall()
	if bool(PrePartNumber) == False:
		result = "Fail"
		measurement = '0'
	elif (PrePartNumber[0])[0] == CurrentPartNumber[0] :
		result = "Pass"
		measurement = '1'
	else:
		result = "Fail"
		measurement = '0'

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
	MeasurementText.insert(END, measurement)

	# Display Result
	ResultText.insert(END, "\n")
	ResultText.insert(END, result)

	if result == "Fail":
		return False
	else:
		return True
