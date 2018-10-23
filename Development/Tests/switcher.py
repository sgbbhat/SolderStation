def Select_Test(name):
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
