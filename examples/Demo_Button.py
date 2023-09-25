''' Demo code to test Button of PiCoder '''

from picoder import BUTTON # Import the BUTTON module from the picoder library
from time import sleep

# Create a button instance named BT1, associated with Button 1 on PiCoder
BT1 = BUTTON(1)

# Continuous loop to read and print the state of BT1
while True:
    # Read the current state of BT1 (pressed or released)
    val1 = BT1.read()
    
    # Print the state of BT1 to the console
    print(f"BT1 = {val1}")
    
    sleep(0.2) #wait for 2 seconds
    
    

