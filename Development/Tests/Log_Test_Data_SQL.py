# Log_Test_Data_SQL
import pyodbc

def Log_Test_Data_SQL(key, val, databaseHandle, mfgID, MessagesLabel):
	#conn = pyodbc.connect('DRIVER={FreeTDS};Server=Waseca-db2;PORT=1433;DATABASE=WasMfg;UID=testpack;PWD=Itron2;TDS_Version=7.4;')
	#cursor = conn.cursor()
	#cursor.execute("Select * from dbo.Part")
	#for row in cursor.fetchall():
	#	print(row)
	print('Running Log Test Data_SQL')
