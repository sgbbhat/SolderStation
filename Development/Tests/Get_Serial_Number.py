# Function runs the stored procedure "getSerialNumber" taking Manufacturing Serial Number as parameters

def getSerialNumber(databaseHandle, mfgID, MessageDisplaySlNo):
	databaseHandle.execute("{CALL [dbo].[getSerialNumber] (?)}", mfgID)
	serialNumber = ((databaseHandle.fetchall())[0])[0]
	MessageDisplaySlNo.config(text = str(serialNumber), anchor = 'w')
	databaseHandle.commit()
	return serialNumber
