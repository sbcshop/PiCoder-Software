''' Demo code to read RFID card value using onboard RFID Module of PiCoder '''

# Import necessary modules from the picoder library and time library
from picoder import BUZZER, RFID
from time import sleep

# Create instances of BUZZER and RFID
buzzer = BUZZER()
rfid = RFID()

# Function to produce a short beep sound using the buzzer
def beep():
    buzzer.on()	
    sleep(0.2)
    buzzer.off()

while True:
    # Read the RFID card value
    cardVal = rfid.read()
    
    # Check if a card value is received (not None)
    if cardVal:
        print(cardVal) # Print the card value to the console
        beep() # Call function to produce a short beep sound
    
    sleep(0.2) # Wait for 0.2 seconds before reading the next card
