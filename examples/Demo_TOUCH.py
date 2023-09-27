''' Demo code to detect coordinates of touch of TFT display of PiCoder'''

from picoder import TOUCH 	# Import the TOUCH module from the picoder library
from time import sleep

# Create an instance of TOUCH
touch = TOUCH()

while True:
    if touch.touched == 1:  # Check if the screen is being touched
        print(touch.touched)
        x, y = touch.getXY()  # Get the X and Y coordinates of the touch, -1 when no touch or any issue
        print(x, y)  # Print the coordinates to the console
    elif touch.touched == 2:
        print(touch.touched)
        lst = touch.touches
        print(lst)
        
    sleep(0.01)  # Wait for a short duration to avoid lagging
