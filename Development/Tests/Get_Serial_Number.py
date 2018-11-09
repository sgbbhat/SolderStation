# Function runs the stored procedure "getSerialNumber" taking Manufacturing Serial Number as input

def getSerialNumber(databaseHandle, mfgID, MessageDisplaySlNo):
	databaseHandle.execute("{CALL [dbo].[getSerialNumber] (?)}", mfgID)	
	serialNumber = int(((databaseHandle.fetchall())[0])[0])
	MessageDisplaySlNo.config(text = str(serialNumber), anchor = 'w')
	databaseHandle.commit()
	return serialNumber
