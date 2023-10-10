''' Security Access System '''

# Import necessary modules from the picoder library and time library
from picoder import BUZZER, RFID, LCD, RGB, SERVO
from time import sleep

# Create instances 
buzzer = BUZZER()
rfid = RFID()
display = LCD()
servo = SERVO()

# Function to produce a short beep sound using the buzzer
def beep():
    buzzer.on()	
    sleep(0.2)
    buzzer.off()

def openGate(): # action when valid card detected
    display.clear()
    display.draw_text8x8(80, 40, "Access Granted", RGB(230, 180, 0))
    beep() # Call function to produce a short beep sound
    servo.move(90)		#open gate
    sleep(2) # wait few seconds
    servo.move(0) # return to initial position
    
def warningMsg(): # action when invalid card detected
    display.clear()
    display.draw_text8x8(80, 40, "Invalid Card", RGB(250, 0, 0))
    beep() # Call function to produce a short beep sound
    sleep(2)
    
    
display.backlight_on() # turn on BackLight of display
display.clear()
display.draw_text8x8(80, 40, 'Security Access System', RGB(230, 180, 0))
sleep(2)
display.clear()

while True:
    # display message on screen
    display.draw_text8x8(80, 40, 'Please Scan Card', RGB(250, 250, 0))
    # Read the RFID card value
    cardVal = rfid.read()
    
    # Check if a card value is received (not None)
    if cardVal is not None:
        print(cardVal) # Print the card value to the console
        
        # now verify authorised card 
        if cardVal == '0796AEA5069C' :
            openGate()	
        else :
            warningMsg()
            
    sleep(0.2) # Wait for 0.2 seconds before reading the next card

