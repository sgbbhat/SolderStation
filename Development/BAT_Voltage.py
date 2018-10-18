# Bat_voltage

def BAT_Voltage(IOPosition, minLimit, maxLimit):
	if IOPosition <  minLimit or IOPosition >  maxLimit:
		return False
	else:
		return True
