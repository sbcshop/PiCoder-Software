''' Demo code to develop some pattern using chaser funtion of LEDMATRIX '''
from picoder import BUZZER, LEDMATRIX
from time import sleep
import utime, random

buzzer = BUZZER()
rgbmatrix = LEDMATRIX()

def beep():
    buzzer.on()
    sleep(0.2)
    buzzer.off()
    
'''rgbmatrix.chaser(startpos, endpos, delay, color = (r, g, b), brightness)'''
r, g, b = 150, 0, 0
rgbmatrix.chaser(0, 64, 0.01, (r, g, b) , 0.01)

while 1:
    r = random.randint(0, 255)	
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgbmatrix.chaser(0, 64, 0.01, (r, g, b) , 0.01)
    beep()

