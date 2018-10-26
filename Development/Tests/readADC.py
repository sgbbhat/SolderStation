from os import *
import time 

while(True):
	#system('megaio 0 aread 1')
	rawScale = popen('megaio 0 aread 1').read()
	scaledV = float(rawScale)/4095.0 * 3.3
	print('Voltage : ' + str(scaledV))
	time.sleep(.200)
