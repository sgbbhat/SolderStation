# Serial_Number

def Serial_Number(databaseHandle, mfgID, MessageDisplaySlNo):
	databaseHandle.execute("Select distinct SerialNumber from dbo.TestEvent WHERE MfgSerialNumber = ?", mfgID)
	serialNumber = databaseHandle.fetchall()
	MessageDisplaySlNo.config(text = str((serialNumber[0])[0]), anchor = 'w')
	return serialNumber
