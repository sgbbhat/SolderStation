# Read Optocoupler
from os import *
import time 

currentState = 0
valChanged = 0

def compareState (current):
	global currentState
	if (int(current) == 0) :
		return 0
	else:
		currentState = 0
		return 1

while (valChanged == 0) :
	currentState = popen('megaio 0 optread 1').read()
	valChanged = compareState(currentState)
	time.sleep(0.5)
