''' Onboard LCD use demo code of PiCoder '''

# import modules from library
from picoder import LED, BUTTON, LCD, RGB 
from time import sleep

# create instance 
display = LCD()
LED1 = LED(1)
LED2 = LED(2)
BT1 = BUTTON(1)
BT2 = BUTTON(2)
BT3 = BUTTON(3)
BT4 = BUTTON(4)

    
def drawButtons():
    display.draw_rectangle(60, 160, 40, 40, RGB(255, 0, 255))
    display.draw_rectangle(120, 160, 40, 40, RGB(0, 255, 255))
    display.draw_rectangle(180, 160, 40, 40, RGB(255, 0, 255))
    display.draw_rectangle(240, 160, 40, 40, RGB(0, 255, 255))
    display.draw_text8x8(68, 220, 'BT1', RGB(20, 20, 255))
    display.draw_text8x8(128, 220, 'BT2', RGB(0, 255, 255))
    display.draw_text8x8(188, 220, 'BT3', RGB(20, 20, 255))
    display.draw_text8x8(248, 220, 'BT4', RGB(0, 255, 255))
    sleep(0.05)

display.backlight_on() # turn on BackLight of display
display.clear()
display.draw_text8x8(80, 40, 'PICO LEARNING KIT', RGB(230, 180, 0))
drawButtons()

while 1:
    #read button status
    val1 = BT1.read()
    val2 = BT2.read()
    val3 = BT3.read()
    val4 = BT4.read()
    
    #fill corresponding button when pressed else clear
    if val1 == 1:
        LED1.on()	#turn on LED1
        display.fill_rectangle(62, 162, 36, 36, RGB(255, 0, 255)) 
    elif val2 == 1:
        LED2.on()	#turn on LED2
        display.fill_rectangle(122, 162, 36, 36, RGB(0, 255, 255))
    elif val3 == 1:
        LED1.on()
        display.fill_rectangle(182, 162, 36, 36, RGB(255, 0, 255))
    elif val4 == 1:
        LED2.on()
        display.fill_rectangle(242, 162, 36, 36, RGB(0, 255, 255))
    else:
        LED1.off()	#turn off LED1
        LED2.off()	#turn off LED2
        display.fill_rectangle(62, 162, 36, 36, RGB(0, 0, 0))
        display.fill_rectangle(122, 162, 36, 36, RGB(0, 0, 0))
        display.fill_rectangle(182, 162, 36, 36, RGB(0, 0, 0))
        display.fill_rectangle(242, 162, 36, 36, RGB(0, 0, 0))
    sleep(0.2)



