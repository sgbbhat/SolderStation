import time
from Serial_Number import Serial_Number
from Enter_Mfg_ID import Enter_Mfg_ID
from Verify_PN import Verify_PN
from Process_Enforcement import Process_Enforcement
from BAT_Voltage import BAT_Voltage
from RST_Voltage import RST_Voltage
from Wakeup_Pulse import Wakeup_Pulse 
from Log_Test_Data_SQL import Log_Test_Data_SQL

StartTime = time.time()
EndTime = time.time()

def Test_Time():
	global EndTime
	global StartTime
	EndTime = time.time()
	TestDuration = EndTime - StartTime
	print(TestDuration)
	return 'Returning Test Time'

switcher = {
		0: Enter_Mfg_ID,
		1: Serial_Number, 
		2: Verify_PN, 
		3: Process_Enforcement, 
		4: BAT_Voltage, 
		6: RST_Voltage, 
		8: Wakeup_Pulse, 
		9: Test_Time, 
		10: Log_Test_Data_SQL
}

TestName = ""
argument = 0

if TestName == "Enter Mfg ID":
	argument = 0
elif TestName == "Serial Number":
	argument = 1
elif TestName == "Verify PN":
	argument = 2
elif TestName == "Process Enforcement":
	argument = 3
elif TestName == "BAT Voltage":
	argument = 4
elif TestName == "BAT Voltage,":
	argument = 5
elif TestName == "RST Voltage":
	argument = 6
elif TestName == "RST Voltage":
	argument = 7
elif TestName == "Wakeup Pulse":
	argument = 8
elif TestName == "Test Time":
	argument = 9
elif TestName == "Log Test Data_SQL":
	argument = 10

while(True):
	print("Enter a number : \n")
	argument = int(input())
	func = switcher.get(argument)
	print(func())
