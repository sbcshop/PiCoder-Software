from picoder import POT, SERVO
from time import sleep
import utime

# Create an instance for respective class
pot = POT() 
servo = SERVO()


while 1:
    # Read the potentiometer value as a percentage (0-100%)
    val_percent = pot.readPercent()
    
    # map the value from percentage into angle 
    angle = servo.servo_Map(val_percent, 0, 100, 0,180)
    
    #move servo to specified angle 
    servo.move(angle)
    sleep(0.1)


