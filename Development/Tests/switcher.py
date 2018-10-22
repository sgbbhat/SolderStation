from Enter_Mfg_ID import Enter_Mfg_ID
from Verify_PN import Verify_PN
from Process_Enforcement import Process_Enforcement
from BAT1_Voltage import BAT1_Voltage
from BAT2_Voltage import BAT2_Voltage
from RST1_Voltage import RST1_Voltage
from RST2_Voltage import RST2_Voltage
from Wakeup_Pulse import Wakeup_Pulse
from Serial_Number import Serial_Number
from Test_Time import Test_Time
from Log_Test_Data_SQL import Log_Test_Data_SQL

def Select_Test(name, param, measurement):
	return {
		"EnterMfgID" : Enter_Mfg_ID, 
		"VerifyPN" : Verify_PN, 
		"ProcessEnforcement" : Process_Enforcement,
		"BAT1Voltage" : BAT1_Voltage,
		"BAT2Voltage" : BAT2_Voltage,
		"RST1Voltage" : RST1_Voltage,
		"RST2Voltage" : RST2_Voltage,
		"WakeupPulse" : Wakeup_Pulse,
		"SerialNumber" : Serial_Number, 
		"TestTime" : Test_Time, 
		"LogTestData_SQL" : Log_Test_Data_SQL,
		} [name]
	
	
