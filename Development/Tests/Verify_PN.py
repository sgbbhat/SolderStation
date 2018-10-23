#Verify_PN

def Verify_PN(key, val, databaseHandle, mfgID, MessagesLabel):
	print('Running Verify PN')
	databaseHandle.execute("Select distinct SerialNumber from dbo.TestEvent WHERE MfgSerialNumber = ?", mfgID)
	partNumber = databaseHandle.fetchall()
	print(partNumber)

#65AAFDWGYAB


# def getSerialNumber(databaseHandle, mfgID, MessageDisplaySlNo):
#	databaseHandle.execute("Select distinct SerialNumber from dbo.TestEvent WHERE MfgSerialNumber = ?", mfgID)
#	serialNumber = databaseHandle.fetchall()
#	MessageDisplaySlNo.config(text = str((serialNumber[0])[0]), anchor = 'w')
#	return serialNumber
