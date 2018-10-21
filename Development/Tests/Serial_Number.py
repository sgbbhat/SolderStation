# Serial_Number

def Serial_Number(databaseHandle, mfgID):
	databaseHandle.execute("Select distinct SerialNumber from dbo.TestEvent WHERE MfgSerialNumber = ?", mfgID)
	serialNumber = databaseHandle.fetchall()
	return serialNumber
