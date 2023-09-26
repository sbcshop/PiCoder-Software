''' Demo code to run Servo motor of PiCoder '''
from picoder import SERVO # Import the SERVO module from the picoder library
from time import sleep	  # Import the sleep function from the time library
import utime			  # Import the utime module for microsecond sleep

# Create an instance of the SERVO class to control the servo motor
s1 = SERVO()

# Move the servo to 100 degrees and wait for 1 second
s1.move(100)
sleep(1)

# Move the servo to 20 degrees and wait for 1 second
s1.move(20)
sleep(1)

while True:
    print("Turn left ...")
    
    # Rotate the servo shaft from 0 to 180 degrees in steps of 5 degrees
    for i in range(0, 180, 5):
        s1.move(i)
        utime.sleep(0.05)
        
    print("Turn right ...")
    
    # Reverse rotation: Rotate the servo shaft from 180 to 0 degrees in steps of 5 degrees
    for i in range(180, 0, -5):
        s1.move(i)
        utime.sleep(0.05)
    
    # Pause for 0.2 seconds between each cycle
    sleep(0.2)
