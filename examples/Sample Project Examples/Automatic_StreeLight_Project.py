''' Automatic Street Light Project'''

''' Idea of project is to switch on street light,
when surrounding light falls below certain threshold value'''

# Import necessary modules from the picoder library and time library
from picoder import LEDMATRIX, LDR
from time import sleep

# Create instances
senseLight = LDR()
light = LEDMATRIX()

threshold = 70 	#change this as per requirement

while True:
    ''' Value increase with increase in darkness level '''
    value = senseLight.readPercent()
    #val = senseLight.read()
    #print(f"val = {val}, value = {value}")
    
    if value > threshold:
        print("Low Light")
        light.on()
    else :
        print("Enough Light")
        light.off()
    sleep(0.5)
    