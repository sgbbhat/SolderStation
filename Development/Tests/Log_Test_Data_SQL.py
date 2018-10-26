# Log_Test_Data_SQL
from tkinter import END
import datetime

def Log_Test_Data_SQL(key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime):
	databaseHandle.execute("Select distinct ProcessFlowKey from dbo.TestEvent WHERE MfgSerialNumber = ? AND ProcessFlowKey != 0", mfgID)
	ProcessFlowKey = databaseHandle.fetchall()	
	TestNameText.get(1.0, END)
	MinLimitText.get(1.0, END)	
	MaxLimitText.get(1.0, END)
	MeasurementText.get(1.0, END)
	searchResult = ResultText.get(1.0, END)
	indexsearchResult = searchResult.find("Fail", 0)
	if indexsearchResult == -1 :
		Passed = 1
	else:
		Passed = 0

	databaseHandle.execute("INSERT INTO dbo.TestEvent (SerialNumber, MfgSerialNumber, PartNumber, ProcessFlowKey, BatchKey, DataCategoryID, StationConfigKey, TestPosition, Attempt, Passed, TestDate, Comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?)", (Sln[0])[0], mfgID, (modelFileContent['Part_No'])[0], int((ProcessFlowKey[0])[0]), 1, 'P', 123, 1, "" , int(Passed), datetime.datetime.now(), "")
	databaseHandle.commit()

	
