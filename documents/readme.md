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
buz = BUZZER()   # create class instance
buz.on() 	      # call function to turn on buzzer
buz.off()	     # to turn off 
```
[Demo Buzzer Example](): this example on Github turns Buzzer on and off in a fixed interval of time.


### (3) BUZZERTONE
BUZZERTONE class is used to control the onboard buzzer, having the facility to create tones depending on Frequency of sound and you can control loudness.
  
**Methods:**
* _play_ :  to turn on Buzzer, this method needs frequency and loudness value as parameters. Integer value of frequency and loudness required.
* _stop_ :  to turn off Buzzer

**Use case:**
```
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
 # interested to Check status of any Button, let say I want to check for BT1
button1 = BUTTON(1)   # create class instance, by passing Button number
value = button1.read()   # call function to read button state and store in variable

```
[Demo Button Example](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Button.py) : checkout demo code how to use the button.

[Combine Testing](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Button_Combine.py) : this example demonstrates use of buttons along with other components. 

