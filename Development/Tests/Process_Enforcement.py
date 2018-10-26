# Process_Enforcement
from tkinter import END

def Process_Enforcement(key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime):
	databaseHandle.execute("Select distinct ProcessFlowKey from dbo.TestEvent WHERE MfgSerialNumber = ? AND ProcessFlowKey != 0", mfgID)
	ProcessFlowKey = databaseHandle.fetchall()
	CurrentPartNumber = modelFileContent['Part_No']
	CurrentProcessStep = 'Board Test'
	databaseHandle.execute("Select PrePartNumber from dbo.ProcessEnforcementStep WHERE ProcessFlowKey = ? AND CurrentPartNumber = ? AND CurrentProcessStep = ?", int((ProcessFlowKey[0])[0]), CurrentPartNumber[0], CurrentProcessStep)
	PrePartNumber = databaseHandle.fetchall()	
	if bool(PrePartNumber) == False:
		PrePartNumberTestResult_lookup = [()]
		PrePartNumberTestResult = [()]
		pass
	else:
		databaseHandle.execute("Select Passed from dbo.InProcess WHERE  MfgSerialNumber = ? AND PartNumber = ? " , mfgID, (PrePartNumber[0])[0])
		PrePartNumberTestResult = databaseHandle.fetchall()
		
	PrePartNumberTestResult_lookup = [item for item in PrePartNumberTestResult if 1 in item]
	if bool(PrePartNumberTestResult_lookup) == False:
		result = "Fail"
		measurement = '0'			
	elif (PrePartNumberTestResult_lookup[0])[0] == 1 :
		result = "Pass"
		measurement = '1'
	else:
		result = "Fail"
		measurement = '0'

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
