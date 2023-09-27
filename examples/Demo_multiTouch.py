''' Demo code for multi touch detection'''

from picoder import TOUCH 	# Import the TOUCH module from the picoder library
from time import sleep

# Create an instance of TOUCH
touch = TOUCH()

while True:
    if touch.touched == 1:  # Check if the screen is being touched
        print(touch.touched)
        x, y = touch.getXY()  # Get the X and Y coordinates of the touch, -1 for any issue
        print(x, y)  # Print the coordinates to the console
    elif touch.touched == 2:
        print(touch.touched)
        #lst = touch.touches
        #print(lst)
        x1, y1, x2, y2 = touch.mgetXY()
        print(f"x1 = {x1} , y1 = {y1}, x2 = {x2}, y2 = {y2}")
        
    sleep(0.1)  # Wait for a short duration to avoid lagging

