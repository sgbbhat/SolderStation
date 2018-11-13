# Log_Test_Data_SQL
from tkinter import END
import datetime

def getTestDefinitionKey(TestName):
	if TestName == 'Verify PN':
		return 488
	elif TestName == 'Process Enforcement':
		return 31
	elif TestName == 'Battery1 Voltage' :
		return 1100
	elif TestName == 'Battery2 Voltage' :
		return 1101
	elif TestName == 'Reset1 Voltage Low' :
		return 1617
	elif TestName == 'Reset2 Voltage Low' :
		return 1618
	elif TestName == 'Reset1 Voltage High' :
		return 1619
	elif TestName == 'Reset2 Voltage High' :
		return 1620
	elif TestName == 'Test Time' :
		return 44 
	elif TestName == 'Startup Detection' :
		return 1622
	elif TestName == 'Battery Voltage After Bridge' :
                return 1666

def Log_Test_Data_SQL(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	if OperationMode == 'Experiment' :
		OperationModeExp = 'E'
	elif OperationMode == 'Production' :
		OperationModeExp = 'P'

	databaseHandle.execute("Select distinct ProcessFlowKey from dbo.TestEvent WHERE MfgSerialNumber = ? AND ProcessFlowKey != 0", mfgID)
	ProcessFlowKey = databaseHandle.fetchall()	
	TestNameTextContent = TestNameText.get(1.0, END)
	MinLimitTextContent = MinLimitText.get(1.0, END)	
	MaxLimitTextContent = MaxLimitText.get(1.0, END)
	MeasurementTextContent = MeasurementText.get(1.0, END)
	searchResult = ResultText.get(1.0, END)
	indexsearchResult = searchResult.find("Fail", 0)
	if indexsearchResult == -1 :
		Passed = 1
	else:
		Passed = 0

	# Insert in to Test Events Table
	timeNow = datetime.datetime.now() 
	testEventParam = (Sln, mfgID, (modelFileContent['Part_No'])[0], 1 ,int((ProcessFlowKey[0])[0]), OperationModeExp, 501 , 1, "" , int(Passed), timeNow, OperationModeInput)
	databaseHandle.execute("{CALL [dbo].[insertTestEvent] (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}", testEventParam)
	TestEventKey = int(((databaseHandle.fetchall())[0])[0])
	databaseHandle.commit()

	# Insert in to Test Event Results
	for test, minlim, maxlim, meas, res in zip(TestNameTextContent.splitlines(), MinLimitTextContent.splitlines(), MaxLimitTextContent.splitlines(), MeasurementTextContent.splitlines(), searchResult.splitlines()) :
		if test == 'Name':
			pass
		else:
			testDefKey = getTestDefinitionKey(test)
			if res == 'Pass' :
				logPass = 1
			else:
				logPass = 0
			testEventResultsParam = (TestEventKey, testDefKey, meas, minlim, maxlim, logPass)
			databaseHandle.execute("{CALL [dbo].[insertTestEventResult] (?, ?, ?, ?, ?, ?)}", testEventResultsParam)
			databaseHandle.commit()

	# Insert in to Component Traceability
	if LotNumvberInput == "" :
		pass
	else :
		vendor, PartNumber, Datecode = LotNumvberInput.split(',')
		param = (mfgID, vendor, PartNumber, Datecode )
		databaseHandle.execute("{CALL [dbo].[InsertComponentTraceability] (?, ?, ?, ?)}", param)
		databaseHandle.commit()

	return True
		
