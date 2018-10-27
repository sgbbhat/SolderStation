import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

# Define a threaded callback function to run in another thread when events are detected  
def my_callback(channel):
	if GPIO.input(14):     # if port 25 == 1  
		print("Rising edge detected on 25")
	else:                  # if port 25 != 1  
		print("Falling edge detected on 25" )
  
# when a changing edge is detected on port 25, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(14, GPIO.BOTH, callback=my_callback)  

try:  
	print("When pressed, you'll see: Rising Edge detected on 25")
	print("When released, you'll see: Falling Edge detected on 25"  )
	sleep(30)         # wait 30 seconds  
	print("Time's up. Finished!" )
finally:                   # this block will run no matter how the try block exits  
	GPIO.cleanup()         # clean up after yourself  
