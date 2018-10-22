# Bat_voltage

def BAT1_Voltage(IOPosition, minLimit, maxLimit):
	if IOPosition <  minLimit or IOPosition >  maxLimit:
		return False
	else:
		return True
