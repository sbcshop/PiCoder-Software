''' Demo code to read distance using Ultrasonic sensor of PiCoder '''
from picoder import ULTRASONIC #import ultrasonic module from picoder library
from time import sleep

distance = ULTRASONIC() #create instance 

while 1:
    value = distance.read() #reads distance in cm
    value_in = distance.read_in() #reads distance in inch
    print(f"Distance is {value} cm, and {value_in} inch ")
    sleep(0.2)
