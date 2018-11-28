# Process_Enforcement
from tkinter import END
import re
from Tests.displayResult import displayResult

def Process_Enforcement(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	# Running a stored procedure - getFlowKey
	getFlowKeyParam = (Sln, (modelFileContent['Part_No'])[0])
	databaseHandle.execute("{CALL [dbo].[getFlowKey] (?, ?)}", getFlowKeyParam)
	ProcessFlowKey = ((databaseHandle.fetchall())[0])[0]
	databaseHandle.commit()

	# Running a stored procedure - getProcessStep
	CurrentPartNumber = (modelFileContent['Part_No'])[0]
	CurrentProcessStep = (modelFileContent['Current_Step'])[0]
	getProcessStepParam = (ProcessFlowKey, CurrentProcessStep, CurrentPartNumber)
	databaseHandle.execute("{CALL [dbo].[getProcessStep] (?, ?, ?)}", getProcessStepParam)
	getProcessStepReturn = databaseHandle.fetchall()
	ProcessStep = (getProcessStepReturn[0])[0]
	PrePartNumber = (getProcessStepReturn[0])[1]
	databaseHandle.commit()

	if bool(PrePartNumber) == False:
		PrePartNumberTestResult_lookup = [()]
		PrePartNumberTestResult = [()]
		pass
	else:
		databaseHandle.execute("Select Passed from dbo.InProcess WHERE  MfgSerialNumber = ? AND PartNumber = ? " , mfgID, CurrentPartNumber)
		PrePartNumberTestResult = databaseHandle.fetchall()

	PrePartNumberTestResult_lookup = [item for item in PrePartNumberTestResult if 1 in item]
	if bool(PrePartNumberTestResult_lookup) == False:
		result = "Fail"
		measurement = 0		
	elif (PrePartNumberTestResult_lookup[0])[0] == 1 :
		result = "Pass"
		measurement = 1
	else:
		result = "Fail"
		measurement = 0

	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display test results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)

	# Return test results
	if result == "Fail":
		return False
	else:
		return True

