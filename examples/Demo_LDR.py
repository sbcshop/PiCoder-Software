''' Demo code to test LDR (Light Dependent Resistor) of PiCoder '''
from picoder import LDR
from time import sleep

# Create an LDR instance
ldr = LDR()

# Continuous loop to read and print LDR values
while True:
    # Read the raw LDR value
    val = ldr.read()
    
    # Read the LDR value as a percentage (0-100%)
    val_percent = ldr.readPercent()
    
    # Print the LDR values to the console
    print(f"LDR Value = {val}, and in percentage = {val_percent}%")
    
    sleep(0.2)  # Wait for 0.2 seconds