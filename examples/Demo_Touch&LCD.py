''' Touch and Display demo of PiCoder kit '''
# import modules from library
from picoder import TOUCH, LCD, RGB 
from time import sleep

# create instance 
display = LCD()
touch = TOUCH()

display.backlight_on() # turn on BackLight of display
display.clear()
display.draw_text8x8(90, 100, 'Touch Screen Demo', RGB(230, 180, 0))
sleep(1)
display.draw_text8x8(80, 100, 'Touch, Hold and Move', RGB(255, 255, 0))
sleep(2)

while True:
    if touch.touched == 1:  # Check if the screen is being touched
        x, y = touch.getXY()  # Get the X and Y coordinates of the touch, -1 for any issue
        #points = 
        print(f"x = {x} , y = {y}")  # Print the coordinates to the console
        display.fill_polygon(3, x, y, 5, RGB(20, 20, 200)) # (n-side, x, y, size, color)
    else :
        display.clear()
    
    sleep(0.01)  # Wait for a short duration to avoid lagging

