''' Demo code to read distance using Ultrasonic sensor of PiCoder '''
from picoder import ULTRASONIC #import ultrasonic module from picoder library
from time import sleep

distance = ULTRASONIC() #create instance 

while 1:
    check = distance.read() #reads distance in cm
    check_in = distance.read_in() #reads distance in inch
    print(f"Distance is {check} cm, and {check_in} inch ")
    sleep(0.2)