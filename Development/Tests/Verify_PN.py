#Verify_PN

def Verify_PN(key, val, databaseHandle, mfgID, MessagesLabel, modelFileContent):
	databaseHandle.execute("Select distinct ProcessFlowKey from dbo.TestEvent WHERE MfgSerialNumber = ? AND ProcessFlowKey != 0", mfgID)
	ProcessFlowKey = databaseHandle.fetchall()
	CurrentPartNumber = modelFileContent['Part_No']
	CurrentProcessStep = 'Board Test'
	databaseHandle.execute("Select PrePartNumber from dbo.ProcessEnforcementStep WHERE ProcessFlowKey = ? AND CurrentPartNumber = ? AND CurrentProcessStep = ?", int((ProcessFlowKey[0])[0]), CurrentPartNumber[0], CurrentProcessStep)
	PrePartNumber = databaseHandle.fetchall()
	if PrePartNumber[0] == CurrentPartNumber[0] :
		return True
	else:
		return False
