''' Demo code to Test Onboard LED on PiCoder '''
from picoder import LED  # Import the LED class from the picoder module
from time import sleep   # Import the sleep function from the time module

# Create an instance of the LED class for LED 1
led1 = LED(1)

# Run an infinite loop
while 1:
    led1.on() # Turn the LED on   
    sleep(0.5) # wait 0.5 seconds

    led1.off() # Turn the LED off
    sleep(0.5) # wait 0.5 seconds
    
    
