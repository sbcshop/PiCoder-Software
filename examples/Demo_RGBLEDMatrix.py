''' Demonstrates how to control an RGB LED of 8x8LED MATRIX on PiCoder '''
from picoder import LEDMATRIX   # Import the LEDMATRIX module from the picoder library 
from time import sleep

# Create an instance of LEDMATRIX
rgbmatrix = LEDMATRIX()

while True:
    # Control all matrix LEDs at once with a specified color and brightness
    r, g, b = 0, 150, 200  # Set the RGB color values (blue-green), 0-255 accepted for each 
    rgbmatrix.on(color=(r,g,b) , brightness=0.02)  # Turn on the LEDs with the specified color and brightness
    sleep(0.5)  # Wait for 0.5 seconds
    rgbmatrix.off()  # Turn off all LEDs
    sleep(0.5)  
    
    # Control individual LEDs
    rgbmatrix.pixelon(0) # Turn on RGB LED at position 1
    sleep(0.5)
    rgbmatrix.pixeloff(0) # Turn off RGB LED at position 1
    
    rgbmatrix.pixelon(5, brightness=0.02)  # Turn on LED at position 6 with specified brightness
    sleep(1)  
    rgbmatrix.pixeloff(5)  # Turn off LED at position 6
    sleep(1)  # Wait for 1 seconds
    
    r, g, b = 200, 150, 0  
    rgbmatrix.pixelon(15, color=(r, g, b), brightness=0.2)  # Turn on LED at position 16 with specified color and brightness
    sleep(1)  
    rgbmatrix.pixeloff(15)  # Turn off LED at position 16
    sleep(1)  
    
    rgbmatrix.pixelon(28, color=(0, 150, 0), brightness=0.8)  
    sleep(1)  
    rgbmatrix.pixeloff(28)  
    sleep(1)  
