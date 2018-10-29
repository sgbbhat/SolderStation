# Log_Test_Data_SQL
from tkinter import END
import datetime

def getTestDefinitionKey(TestName):
	if TestName == 'VerifyPN':
		return 488
	elif TestName == 'ProcessEnforcement':
		return 31
	elif TestName == 'BAT1Voltage' :
		return 1100
	elif TestName == 'BAT2Voltage' :
		return 1101
	elif TestName == 'RST1VoltageLow' :
		return 1617
	elif TestName == 'RST2VoltageLow' :
		return 1618
	elif TestName == 'RST1VoltageHigh' :
		return 1619
	elif TestName == 'RST2VoltageHigh' :
		return 1620
	elif TestName == 'TestTime' :
		return 44 

def Log_Test_Data_SQL(key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime):
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
	databaseHandle.execute("INSERT INTO dbo.TestEvent (SerialNumber, MfgSerialNumber, PartNumber, ProcessFlowKey, BatchKey, DataCategoryID, StationConfigKey, TestPosition, Attempt, Passed, TestDate, Comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?)", (Sln[0])[0], mfgID, (modelFileContent['Part_No'])[0], int((ProcessFlowKey[0])[0]), 1, 'P', 501 , 1, "" , int(Passed), timeNow, "")
	databaseHandle.commit()
	
	# Get Test Event Key
	databaseHandle.execute("Select TestEventKey from dbo.TestEvent WHERE TestDate = ? AND PartNumber = ? AND MfgSerialNumber = ? ", timeNow, (modelFileContent['Part_No'])[0], mfgID)
	TestEventKey = int(((databaseHandle.fetchall())[0])[0])

	# Insert in to Test Event Results
	#databaseHandle.execute("INSERT INTO dbo.TestEventResult (TestEventKey, ) VALUES (?, ?, ?, ?, ?, ?)",)
	#databaseHandle.commit()
	for test, minlim, maxlim, meas, res in zip(TestNameTextContent.splitlines(), MinLimitTextContent.splitlines(), MaxLimitTextContent.splitlines(), MeasurementTextContent.splitlines(), searchResult.splitlines()) :
		if test == 'Name':
			pass
		else:
			testDefKey = getTestDefinitionKey(test)
			if res == 'Pass' :
				logPass = 1
			else:
				logPass = 0
			#print(test + " " +  maxlim + " " + minlim + " " + meas + " " + res + " " + str(testDefKey))
			databaseHandle.execute("INSERT INTO dbo.TestEventResult (TestEventKey, TestDefinitionKey, Measurement, MinLimit, MaxLimit, Passed) VALUES (?, ?, ?, ?, ?, ?)",TestEventKey, testDefKey, meas, minlim, maxlim, logPass)
			databaseHandle.commit()
		
