''' Demo code to detect coordinates of touch of TFT display of PiCoder'''

from picoder import TOUCH 	# Import the TOUCH module from the picoder library
from time import sleep

# Create an instance of TOUCH
touch = TOUCH()

while True:
    if touch.touched == 1:  # Check if the screen is being touched
        x, y = touch.getXY()  # Get the X and Y coordinates of the touch, -1 for any issue
        print(f"x = {x} , y = {y}")  # Print the coordinates to the console
        
    sleep(0.05)  # Wait for a short duration to avoid lagging
