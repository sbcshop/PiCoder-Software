''' Demo code to test Buttons of PiCoder,
Combine operation is demonstrated here with LED, buzzer and Relay
'''
from picoder import LED, BUZZER, RELAY, BUTTON # import required class from module
from time import sleep

#create object for each class to access methods
led1 = LED(1)
led2 = LED(2)
relay1 = RELAY(1)
relay2 = RELAY(2)
buzzer = BUZZER()
BT1 = BUTTON(1)
BT2 = BUTTON(2)
BT3 = BUTTON(3)
BT4 = BUTTON(4)

#function which on and off buzzer
def beep():
    buzzer.on()
    sleep(0.2)
    buzzer.off()
    

while 1:
    val1 = BT1.read()	#read button states, normally 0 and 1 when pressed
    val2 = BT2.read()
    val3 = BT3.read()
    val4 = BT4.read()
    
    if val1 == 1:	# logic check, true when button pressed
        led1.on()	# Turn on LED1
        beep()		# beeps buzzer
        led1.off()	# Turn off LED1
        
    if val2 == 1:
        led2.on()	# Turn on LED2
        beep()
        led2.off()	# Turn off LED2
    
    if val3 == 1:
        relay1.on()		# Turn on RELAY1
        beep()
        relay1.off()	# Turn off RELAY1
    
    if val4 == 1:
        relay2.on()		# Turn on RELAY2
        beep()
        relay2.off()	# Turn off RELAY2
    
    print(f"BT1 = {val1}, BT2 = {val2}, BT3 = {val3}, BT4 = {val4}")
    sleep(0.2) #wait for some time
