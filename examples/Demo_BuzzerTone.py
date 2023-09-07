''' This code demonstrate how to play different tones on Buzzer '''

from picoder import BUZZERTONE  # Import the BUZZERTONE class from the picoder module
from time import sleep   # Import the sleep function from the time module

# Create an instance of the BUZZERTONE class
bzrtone = BUZZERTONE()

# Run an infinite loop
while 1:
    bzrtone.play(512,5000) #send frequency, loudness to play tone on Buzzer. Loudness -> 0-5000
    sleep(0.5)
    
    bzrtone.stop() #to stop buzzer
    sleep(0.5)

    


