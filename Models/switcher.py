import time

StartTime = time.time()
EndTime = time.time()

def Enter_Mfg_ID():
	global StartTime
	StartTime = time.time()
	return "Returning Enter Mfg ID"

def Serial_Number():
	return 'Returning Serial Number'

def Verify_PN():
	return 'Returning Verify PN'

def Process_Enforcement():
	return 'Returning Process Enforcement'

def BAT1_Voltage():
	return 'Returning BAT1 Voltage'

def BAT2_Voltage():
	return 'Returning BAT2 Voltage'

def RST1_Voltage():
	return 'Returning RST1 Voltage'

def RST2_Voltage():
	return 'Returning RST2 Voltage'

def Wakeup_Pulse():
	return 'Returning Wakeup Pulse'

def Test_Time():
	return 'Returning Test Time'

def Log_Test_Data_SQL():
	global EndTime
	global StartTime
	EndTime = time.time()
	TestDuration = EndTime - StartTime
	print(TestDuration)
	return 'Returning Log Test Data_SQL'

switcher = {
		0: Enter_Mfg_ID,
		1: Serial_Number, 
		2: Verify_PN, 
		3: Process_Enforcement, 
		4: BAT1_Voltage, 
		5: BAT2_Voltage, 
		6: RST1_Voltage, 
		7: RST2_Voltage, 
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
elif TestName == "BAT1 Voltage":
	argument = 4
elif TestName == "BAT2 Voltage,":
	argument = 5
elif TestName == "RST1 Voltage":
	argument = 6
elif TestName == "RST2 Voltage":
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
