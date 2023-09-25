''' Demo code to test the onboard Potentiometer of PiCoder '''

from picoder import POT	 # Import the POT module from the picoder library
from time import sleep

# Create an instance of the POT class to access the onboard potentiometer
pot = POT()

# Continuous loop to read and print the potentiometer value
while True:
    # Read the raw value of the potentiometer
    val = pot.read()
    
    # Read the potentiometer value as a percentage (0-100%)
    val_percent = pot.readPercent()
    
    # Print the raw value and the value in percentage to the console
    print(f"Pot Value = {val}, and in percentage = {val_percent}%")
    
    # Pause for 0.2 seconds before the next reading
    sleep(0.2)


