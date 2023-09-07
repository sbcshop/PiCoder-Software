''' Demo code to Test Buzzer on PiCoder '''
from picoder import BUZZER  # Import the Buzzer class from the picoder module
from time import sleep   # Import the sleep function from the time module

# Create an instance of the Buzzer class
bzr = BUZZER()

# Run an infinite loop
while 1: 
    bzr.on() # Turn the LED on   
    sleep(0.5) # wait 0.5 seconds

    bzr.off() # Turn the LED off
    sleep(0.5) # wait 0.5 seconds
    
    

