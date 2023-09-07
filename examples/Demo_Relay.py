''' Demo code for onboard Relay control of PiCoder '''
from picoder import RELAY  # Import the RELAY class from the picoder module
from time import sleep   # Import the sleep function from the time module

# Create an instance of the RELAY class for RELAY 2
relay = RELAY(2)

# Run an infinite loop
while 1:
    relay.on() # Turn the RELAY on   
    sleep(0.5) # wait 0.5 seconds

    relay.off() # Turn the RELAY off
    sleep(0.5) # wait 0.5 seconds
    
    

