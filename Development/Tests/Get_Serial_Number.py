
def getSerialNumber(databaseHandle, mfgID, MessageDisplaySlNo):
	databaseHandle.execute("Select distinct SerialNumber from dbo.TestEvent WHERE MfgSerialNumber = ? AND SerialNumber != 0", mfgID)
	serialNumber = databaseHandle.fetchall()
	MessageDisplaySlNo.config(text = str((serialNumber[0])[0]), anchor = 'w')
	return serialNumber
