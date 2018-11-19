# Process_Enforcement
from tkinter import END
import re
from Tests.displayResult import displayResult

def Process_Enforcement(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	databaseHandle.execute("Select distinct ProcessFlowKey from dbo.TestEvent WHERE MfgSerialNumber = ? AND ProcessFlowKey != 0", mfgID)
	ProcessFlowKey = databaseHandle.fetchall()
	CurrentPartNumber = modelFileContent['Part_No']
	CurrentProcessStep = 'Board Test'
	databaseHandle.execute("Select PrePartNumber from dbo.ProcessEnforcementStep WHERE ProcessFlowKey = ? AND CurrentPartNumber = ? AND CurrentProcessStep = ?", int((ProcessFlowKey[0])[0]), CurrentPartNumber[0], CurrentProcessStep)
	PrePartNumber = databaseHandle.fetchall()
	print(PrePartNumber)	
	if bool(PrePartNumber) == False:
		PrePartNumberTestResult_lookup = [()]
		PrePartNumberTestResult = [()]
		pass
	else:
		databaseHandle.execute("Select Passed from dbo.InProcess WHERE  MfgSerialNumber = ? AND PartNumber = ? " , mfgID, 'ERG7100005-Curie')
		PrePartNumberTestResult = databaseHandle.fetchall()

	print(PrePartNumberTestResult)
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

