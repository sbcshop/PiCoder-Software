""" Demo code to display image on PiCoder """
#import library 
from time import sleep
from picoder import LCD

display = LCD() # create instance


def displayImg():
    display.draw_image('river.raw', 0, 0, 320, 240) # display raw image file, change name as per your filename
    sleep(200)
    display.cleanup()

displayImg()