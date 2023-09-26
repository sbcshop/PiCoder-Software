## [PiCoder Library](https://github.com/sbcshop/PiCoder-Software/blob/main/picoder.py) : 

The [picoder.py](https://github.com/sbcshop/PiCoder-Software/blob/main/picoder.py) module is designed to make it simple to work with the various PiCoder onboard components. As a result, creating cool projects with the PiCoder kit takes less time because no specialised interface coding is required. This will help you to get start quickly.

Each onboard component is represented by the following essential Class in the module. There are also several supporting classes included in the module.


### (1) LED
LED class is used to control onboard two LEDs. You will have to pass parameters as a choice of LED 1 or 2. Else you can pass GPIO number of Pico W to which external LEDs are connected on the breadboard.
 
**Methods:**
* _on_ :  this method is used to turn on LED
* _off_ :  this method is used to turn off LED

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
  
**Methods:**
* _on_ :  to turn on Buzzer
* _off_ :  to turn off Buzzer

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
  
**Methods:**
* _play_ :  to turn on Buzzer, this method needs frequency and loudness value as parameters. Integer value of frequency and loudness required.
* _stop_ :  to turn off Buzzer

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
 
**Methods:**
* _on_ :  this method is used to turn on RELAY
* _off_ :  this method is used to turn off RELAY

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
 
**Methods:**
* _read_ :  to read status of respective button

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
 
**Methods:**
* _read_ :  to read the raw value in integer
* _readPercentage_ :  to read the value in percentage from 0-100%

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
 
**Methods:**
* _move_ : to move servo motor shaft at an angle pass from 0-180 degree.
* _middle_ :  to move the servo motor shaft at middle position.
* _servo_Map_ :  
    - to change the value from one range to another, useful when converting POT value into angle.
    - servo_Map(value, from_min, from_max, to_min, to_max)

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
 
**Methods:**
* _read_  :  to read the raw value in integer
* _readPercent_ :  to read the value in percentage from 0-100%

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
 
**Methods:**
* _temperature_ :  to read the temperature in degrees
* _pressure_ :  to read the pressure in hPa
* _humidity_ :  to read the relative humidity in %

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

### (9) ULTRASONIC 
The ULTRASONIC class is used to read the distance of an object in front of the ultrasonic sensor of PiCoder.

**Methods:**
* _read_ :  to read the distance in cm
* _read_in_ :  to read the distance in inch

Use case:
```
#import required module from library
from picoder import ULTRASONIC

distance = ULTRASONIC() #create instance 
Value = distance.read() #reads distance in cm
Value_in = distance.read_in() #reads distance in inch

```
 
[Ultrasonic Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_UltrasonicSensor.py) : Demo code to read distance of object in cm and inch value.
