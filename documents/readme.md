## [PiCoder Library](https://github.com/sbcshop/PiCoder-Software/blob/main/picoder.py) : 

The [picoder.py](https://github.com/sbcshop/PiCoder-Software/blob/main/picoder.py) module is designed to make it simple to work with the various PiCoder onboard components. As a result, creating cool projects with the PiCoder kit takes less time because no specialised interface coding is required. This will help you to get start quickly.

Each onboard component is represented by the following essential Class in the module. There are also several supporting classes included in the module.

Module Content ->

- [LED](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#1-led)
- [BUZZER](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#2-buzzer)
- [BUZZERTONE](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#3-buzzertone)
- [RELAY](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#4-relay)
- [BUTTON](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#5-button)
- [POT](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#6-pot)   
- [SERVO](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#7-servo)
- [LDR](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#8-ldr) 
- [BME280](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#9-bme280)   
- [ULTRASONIC](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#10-ultrasonic)
- [RFID](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#11-rfid) 
- [LEDMATRIX](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#12-ledmatrix)
- [TOUCH](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#13-touch)
- [RGB]() 
- [LCD](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#15-lcd)

### (1) LED
LED class is used to control onboard two LEDs. You will have to pass parameters as a choice of LED 1 or 2. Else you can pass GPIO number of Pico W to which external LEDs are connected on the breadboard.
 
|Method | Function |
|---|---|
|_on_ | used to turn on LED |
|_off_ | used to turn off LED |

**Use case:**
```
# import required module from library
from picoder import LED

# interested to work with LED1
Led1 = LED(1)   # create class instance, by passing LED number
Led1.on() 	  # call function to turn on LED 1 of PiCoder
```
[Demo LED Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_LED.py): this example on Github turns led on and off in a fixed interval of time.

### (2) BUZZER
BUZZER class is used to control the onboard buzzer. Includes a straightforward way for turning on and off a buzzer with a fixed tone.
No parameters required to pass if using an onboard buzzer. Pass GPIO number if using external buzzer.
  
|Method | Function |
|---|---|
|_on_ | used to turn on Buzzer |
|_off_ | used to turn off Buzzer |

**Use case:**
```
# import required module from library
from picoder import BUZZER

buz = BUZZER()   # create class instance
buz.on() 	      # call function to turn on buzzer
buz.off()	     # to turn off 
```
[Demo Buzzer Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Buzzer.py): this example on Github turns Buzzer on and off in a fixed interval of time.


### (3) BUZZERTONE
BUZZERTONE class is used to control the onboard buzzer, having the facility to create tones depending on Frequency of sound and you can control loudness.

|Method | Function |
|---|---|
|_play_ | to turn on Buzzer, this method needs frequency and loudness value as parameters |
|_stop_ | to turn off Buzzer |

**Use case:**
```
# import required module from library
from picoder import BUZZERTONE

buz = BUZZERTONE()   # create class instance
Freq = 1024          # change to see different tone
loudness = 2000      # Higher the louder, close to 0 reduce sound intensity
buz.play(freq, loudness)  # call function to on buzzer with some tone
buz.stop()	     # to turn off buzzer 
```

[Buzzer Tone Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_BuzzerTone.py): this example shows how to create tone with buzzer.

### (4) RELAY
RELAY class is used to control onboard two RELAY . You will have to pass parameters as a choice of RELAY 1 or 2. 
Alternatively, you can pass the GPIO number of Pico W to which external Relays are connected on the breadboard.

|Method | Function |
|---|---|
|_on_ | to turn on RELAY |
|_off_ | to turn off RELAY |

Use case:
```
# import required module from library
from picoder import RELAY

 # interested to work with RELAY2
relay = RELAY(2)   # create class instance, by passing RELAY number
relay.on() 	       # call function to turn on RELAY 2 of PiCoder
```

[Demo Relay Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Relay.py) : this example on Github turns the relay on and off in a fixed interval of time.

### (5) BUTTON
BUTTON class is used to check button status. You will have to pass parameters as a choice of onboard Button 1, 2, 3 or 4. 
Alternatively, you can pass the GPIO number of Pico W to which external buttons are connected on the breadboard.

|Method | Function |
|---|---|
|_read_ | to read status of respective button, return logic 1 when pressed else 0 |

Use case:
```
# import required module from library
from picoder import BUTTON

 # interested to Check status of any Button, let say I want to check for BT1
button1 = BUTTON(1)   # create class instance, by passing Button number
value = button1.read()   # call function to read button state and store in variable

```
[Demo Button Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Button.py) : checkout demo code how to use the button.

[Combine Testing](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Button_Combine.py) : this example demonstrates use of buttons along with other components. 


### (6) POT
POT class is used to read the value of onboard Potentiometer. 

|Method | Function |
|---|---|
|_read_ | to read the raw value in integer |
|_readPercentage_ | to read the value in percentage from 0-100% |

Use case:
```
# import required module from library
from picoder import POT

# Create an instance of the POT class to access the onboard potentiometer
pot = POT()    
val = pot.read()  # Read the raw value of the potentiometer
val_percent = pot.readPercent()  # value in percentage

```
[Demo POT Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_POT.py) : checkout demo code how to read value of potentiometer of PiCoder.

### (7) SERVO
The SERVO class is used to rotate the onboard servo motor shaft to a specified angle.

|Method | Function |
|---|---|
|_move_ | to move servo motor shaft at an angle pass from 0-180 degree |
|_middle_ | to move the servo motor shaft at middle position |
|_servo_Map_ | to change the value from one range to another, useful when converting POT value into angle |

Use case:
```
# import required module from library
from picoder import SERVO

# Create an instance of the SERVO class to control the servo motor
s1 = SERVO()

# Move the servo to 100 degrees
s1.move(100)

# Read the potentiometer value as a percentage (0-100%)
val_percent = pot.readPercent()
    
# map the value from percentage into angle 
angle = s1.servo_Map(val_percent, 0, 100, 0,180)
s1.move(angle)

```
[Servo Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Servo.py): checkout demo code for servo motor to move at certain angle.

[Servo_POT Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Servo_POT.py): The servo shaft is rotated by the POT value.

### (8) LDR 
LDR class is used to get the reading of an LDR (Light Dependent Resistor) sensor to detect presence of Light.

|Method | Function |
|---|---|
|_read_ | to read the raw value in integer |
|_readPercent_ | to read the value in percentage from 0-100% |

Use case:
```
# import required module from library
from picoder import LDR

# Create an instance of the POT class to access the onboard potentiometer
ldr = LDR()   
# Read the raw LDR value
val = ldr.read()
    
# Read the LDR value as a percentage (0-100%)
val_percent = ldr.readPercent()

```
[LDR Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_LDR.py): Demo code to read and display LDR sensor value.


### (9) BME280 
BME280 class is used to get the value of Temperature, Pressure and Humidity from the BME280 sensor.

|Method | Function |
|---|---|
|_temperature_ | to read the temperature in degrees |
|_pressure_ | to read the pressure in hPa |
|_humidity_ | to read the relative humidity in % |

Use case:
```
# import required module from library
from picoder import BME280

#create instance of class
sense = BME280()

t = sense.temperature() # provides temperature in Degrees
p = sense.pressure() 	# provides pressure in hPa
h = sense.humidity()	# provides relative Humidity in percentage

```
[BME280 Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_BME280.py): Code gives idea how to read temperature, pressure and humidity from BME280 of PiCoder.

### (10) ULTRASONIC 
The ULTRASONIC class is used to read the distance of an object in front of the ultrasonic sensor of PiCoder.

|Method | Function |
|---|---|
|_read_ | to read the distance in cm |
|_read_in_ | to read the distance in inch |

Use case:
```
#import required module from library
from picoder import ULTRASONIC

distance = ULTRASONIC() #create instance 
Value = distance.read() #reads distance in cm
Value_in = distance.read_in() #reads distance in inch

```
 
[Ultrasonic Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_UltrasonicSensor.py) : Demo code to read distance of object in cm and inch value.

### (11) RFID
The RFID class is used to read 125KHz RFID cards using the onboard RFID module of PiCoder.

|Method | Function |
|---|---|
|_read_ | to read the RFID card value |

Use case:
```
#import required module from library
from picoder import RFID

# Create instances of RFID
rfid = RFID()

# Read the RFID card value
cardVal = rfid.read()

```
 
[RFID Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_RFID_module.py) : checkout example code how to read RFID card using onboard Module of PiCoder.


### (12) LEDMATRIX
The LEDMATRIX class contains methods to control RGB LEDs of 8X8 LED MATRIX. Both options are available to control a single LED or all at once. 

|Method | Function |
|---|---|
|_on_ | used to turn ON all 64 LEDs in one go, even you can send color and brightness value for effective control |
|_off_ | used to turn OFF all LEDs of matrix |
|_pixelon_ | used to TURN ON single RGB LED. You need to pass integer value 0-63 of LED to turn on out of 64. Here also you can decide RGB color and brightness value |
|_pixeloff_ | used to TURN OFF specific LEDs. So, pass the LED number as a parameter. |
|_chaser_ |  this function generates a kind of pattern which turns on and off LEDs in sequence from 0-63 and reverse. |

Use case:
```
#import required module from library
from picoder import LEDMATRIX

# Create an instance of LEDMATRIX
rgbmatrix = LEDMATRIX()

'''
WARNING: AVOID Direct Looking at matrix when using on() method without brightness control,
default full brightness is very HIGH may cause trouble to EYES
'''
rgbmatrix.on() # to Turn ON all LEDs with default white color
rgbmatrix.off() # to Turn OFF all LEDs

rgbmatrix.on(color=(200,150,0) , brightness=0.02) # with color and brightness control

# to control single RGB LED
rgbmatrix.pixelon(4) # Turn ON RGB LED at position 5
rgbmatrix.pixeloff(4) # Turn OFF LED at position 5

rgbmatrix.pixelon(28, color=(0, 150, 0), brightness=0.8)  # Turn ON with color and brightness value
rgbmatrix.pixeloff(28) # Turn OFF 

```
WARNING: AVOID Direct Looking at matrix when using on() method without brightness control, default full brightness is very HIGH may cause trouble to EYES

[RGB LED Matrix Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_RGBLEDMatrix.py) : The code includes functions to control all LEDs at once, individual LEDs, and set specific colors and brightness levels.

[RGBChaserPattern](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/RGBChaserPattern.py) : checkout pattern generation demo code.

### (13) TOUCH
The TOUCH class is to detect the coordinates of the display where the screen is touched. There are also methods to detect single or multi-touch (two-point).

|Method | Function |
|---|---|
|_touched_ | property to check if the screen is touched and returns a number of touches |
|_touches_ | property  to get coordinates of touches in a list with ID number |
|_getXY_ | function returns X and Y coordinates of the touch if within resolution range 320x240, else -1 for out of range or any error. Use when a single touch is detected. |
|_mgetXY_ | function returns 4 values x1, y1, x2 and y2. Use for multi-touch. |

Use case:
```
#import required module from library
from picoder import TOUCH

# Create an instance of TOUCH
touch = TOUCH()

if touch.touched == 1:  # Check if the screen is being touched
        x, y = touch.getXY()  # Get the X and Y coordinates of the touch, -1 for any issue

```
[Touch Detect Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_TOUCH.py) : demonstrates how to use the TOUCH module from library to detect and print touch coordinates (X, Y) when the screen is touched.

[Multi-Touch Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_multiTouch.py) : how to detect two point touch on screen.

### (14) RGB
RGB is a method inside the picoder module for converting RGB888 color to 16 bit RGB565 for LCD display.

Use case:
```
#import module as shown below
from picoder import RGB

color = RGB(255, 200, 25) # will generate 16 bit RGB565 format
```

### (15) LCD
The LCD class contains various methods to work with an onboard 3.2” TFT display of PiCoder. 

| Method | Function |
|---|---|
|_backlight_on_  | to turn ON backlight of display |
|_backlight_off_  | to turn ON backlight of display |
|_display_on_     | to turn ON display |
|_display_off_    | to turn OFF display |
|_clear_          | to clear display |
|_cleanup_        | to clean and free up resources |
|_draw_circle_    | to draw a circle|
|_fill_circle_    | to draw a filled circle|
|_draw_ellipse_   | to draw a ellipse|  
|_fill_ellipse_   | to draw a filled ellipse|
|_draw_rectangle_ | to draw a rectangle|  
|_fill_rectangle_ | to draw a filled rectangle|
|_draw_polygon_   | to draw an n-sided regular polygon|
|_fill_polygon_   | to fill n-sided regular polygon  
|_draw_hline_     | to draw horizontal line| 
|_draw_vline_     | to draw vertical line|  
|_draw_line_      | to draw a line|
|_draw_lines_     | to draw multiple lines|
|_draw_pixel_     | to draw a single pixel|
|_fill_hrect_     | to draw a filled rectangle (optimized for horizontal drawing)|
|_fill_vrect_     | to draw filled rectangle (optimized for vertical drawing)
|_draw_letter_    | to draw a letter|
|_draw_text_      | to draw text|
|_draw_text8x8_   | to draw text using built-in MicroPython 8x8 bit font|
|_draw_sprite_    | to draw a sprite (optimized for horizontal drawing)|
|_load_sprite_    | to load sprite image|
|_draw_image_     | to draw image from flash|
|_set_scroll_     | to set the height of the top and bottom scroll margins|
|_scroll_         | to scroll display vertically|
|_is_off_grid_    | to check if coordinates extend past display boundaries|

**Note:** Requirement for any graphics color is 16 bit RGB565 which is achieved using method RGB(r, g, b) which returns converted 16 bit color format.

Use case:
```
#import required module from library
from picoder import LCD, RGB

# Create an instance of LCD
display = LCD()

display.backlight_on()
display.draw_rectangle(0, 0, 320, 240, RGB(255, 0, 255))
display.draw_text8x8(90, 20, 'PICO LEARNING KIT', RGB(0, 255, 0))

```
Check below demo codes how to use methods of LCD for display,
- [LCD Demo Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_LCD.py)
- [Graphics Demo](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Graphics.py)
- [Touch & LCD Demo](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Touch%26LCD.py)
