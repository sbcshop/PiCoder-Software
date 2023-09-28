''' Demo code to create Graphics on display of PiCoder '''

# import modules from library
from picoder import LCD, RGB 
from time import sleep

# create instance of LCD 
display = LCD()


def circleDemo():
    display.clear()
    
    '''
    parameters => (x0, y0, r, color)
        x0 (int): X coordinate of center point.
        y0 (int): Y coordinate of center point.
        r (int): Radius.
        color (int): RGB565 color value.
    '''
    display.draw_circle(240,180, 40, RGB(255, 255, 255))
    display.fill_circle(240,180, 20, RGB(250, 0, 120))
    display.draw_circle(100, 100, 60, RGB(0, 150, 0))
    sleep(1)

def ellipseDemo():
    display.clear()
    
    '''
    parameters => (x0, y0, a, b, color)
        x0, y0 (int): Coordinates of center point.
        a (int): Semi axis horizontal.
        b (int): Semi axis vertical.
        color (int): RGB565 color value.
    '''
    
    display.draw_ellipse(100, 60, 80, 40, RGB(255, 255, 255))
    display.fill_ellipse(70, 200, 40, 12, RGB(255, 0, 10))
    
    display.draw_ellipse(200, 200, 40, 30, RGB(200, 0, 10))
    display.fill_ellipse(200, 200, 38, 28, RGB(10, 150, 100))
    sleep(1)
    
    
def rectangleDemo():
    display.clear()
    
    '''
    parameters => (x, y, w, h, color)
        x (int): Starting X position.
        y (int): Starting Y position.
        w (int): Width of rectangle.
        h (int): Height of rectangle.
        color (int): RGB565 color value.
    '''

    display.draw_rectangle(20, 30, 100, 50, RGB(200, 20, 200))
    display.fill_rectangle(25, 40, 60, 30, RGB(200, 20, 200))
    display.draw_rectangle(200, 30, 40, 180, RGB(20, 20, 180))
    
    display.fill_hrect(100, 90, 80, 60, RGB(200, 20, 80))
    display.fill_vrect(120, 100, 50, 90, RGB(210, 210, 120))
    sleep(2)

def polygonDemo():
    display.clear()
    
    '''
    parameters => (sides, x0, y0, r, color, rotate=0)
        sides (int): Number of polygon sides.
        x0, y0 (int): Coordinates of center point.
        r (int): Radius.
        color (int): RGB565 color value.
        rotate (Optional float): Rotation in degrees relative to origin.
    '''

    display.draw_polygon(5, 200, 100, 60, RGB(250, 150, 0), 10)
    display.fill_polygon(3, 70, 200, 30, RGB(25, 200, 200))
    display.fill_polygon(8, 70, 50, 30, RGB(200, 200, 200))
    sleep(2)
    
def lineDemo():
    display.clear()
    '''
    parameters required=> (x1, y1, x2, y2, color)
        x1, y1 (int): Starting coordinates of the line
        x2, y2 (int): Ending coordinates of the line
        color (int): RGB565 color value.
    '''
    display.draw_line(20, 30, 250, 180, RGB(140, 150, 200))
    
     
    '''
    horizontal and vertical line example
    parameters required=> (x, y, h, color)
        x (int): Starting X position.
        y (int): Starting Y position.
        h (int): Height of line.
        color (int): RGB565 color value.
    '''
    display.draw_hline(40, 50, 250, RGB(0, 10, 200))
    display.draw_vline(160, 40, 200, RGB(255, 0, 255))
    sleep(1)

    
display.backlight_on() # Turn ON backlight of Display

circleDemo()
rectangleDemo()
ellipseDemo()
lineDemo()
polygonDemo()

    




