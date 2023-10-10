''' Automatic Garage Door Opening'''

# Import necessary modules from the picoder library and time library
from picoder import BUZZER, ULTRASONIC, SERVO
from time import sleep

# Create instances
distance = ULTRASONIC()
buzzer = BUZZER()
servo = SERVO()

# Function to produce a short beep sound using the buzzer
def beep():
    buzzer.on()	
    sleep(0.2)
    buzzer.off()

def opengate():
    beep()
    servo.move(90)	#Gate open
    sleep(4)
    for i in range(3): #alert before closing gate 
        beep()
        sleep(0.2)
    servo.move(0)	#close gate
    
threshold = 7 	#change this as per requirement
servo.move(0)   #initially close gate

while True:
    ''' Value increase with increase in darkness level '''
    value = distance.read()
    print(f"distance value = {value} cm")
    
    if value < threshold:
        print("Open Gate")
        opengate()

    sleep(1)
    
