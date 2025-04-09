# PiCoder - Pico Learning Kit
100% DIY | 100% Programmable| L&D | RPi Pico | LED Matrix | LDR | 3.2" Touch LCD | BME280 | Ultrasonic Sensor | RFID | Dual USB | POT

A compact and comprehensive Raspberry Pi Pico W based Learning Kit having onboard actuators, sensors, and LEDs makes learning enjoyable.


<img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_banner.jpg">

The PiCoder is loaded with many features that are going to help you learn and explore many opportunities in the field of computer science and electronics.

PiCoder is an all-in-one STEM learning kit that allows students to work directly with the most common hardware components used in DIY projects. 
Features the most well-known Raspberry Pi Pico, which enjoys strong community support.The most popular programming languages, Micropython, Ciruitpython, and Arduino, are supported across platforms.

Because the lesson for the PiCoder kit is mostly based on Micropython, it is advised that you understand the very fundamentals of Python.
This GitHub provides details and step-by-step instructions how to use PiCoder kit. 

### 📑 Table of Contents
1. [Pinout](https://github.com/sbcshop/PiCoder-Software/tree/main#pinout)
2. [Getting Started with PiCoder ](https://github.com/sbcshop/MicroFlex_MCU_Software/edit/main/MicroFlex%20with%20Arduino%20IDE/readme.md#-running-examples)
    * [How to Install Boot Firmware in Pico W of PiCoder kit](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#1-how-to-install-boot-firmware-in-pico-w-of-picoder-kit)
    * [Running First Program in PiCoder](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#2-running-first-program-in-picoder)
    * [How to Move Script Codes or Any Files to PiCoder](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#3-how-to-move-script-codes-or-any-files-to-picoder)
3. [Lessons](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lessons)
    * [Lesson 1 : How to Blink LED](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-1--how-to-blink-led)
    * [Lesson 2 : How to Play Buzzer of PiCoder](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-2--how-to-play-buzzer-of-picoder)
    * [Lesson 3 : Read Value of POT](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-3--read-value-of-pot)
    * [Lesson 4 : How to Rotate Servo Motor](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-4--how-to-rotate-servo-motor)
    * [Lesson 5 : How to Check Status of Button](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-5--how-check-status-of-button)
    * [Lesson 6 : How to Read LDR Sensor for Light Detection ](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-6--how-to-read-ldr-sensor-for-light-detection)
    * [Lesson 7 : How to Read BME280 Sensor of PiCoder](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-7---how-to-read-bme280-sensor-of-picoder)
    * [Lesson 8 : How to use Ultrasonic Sensor of PiCoder](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-8--how-to-use-ultrasonic-sensor-of-picoder)
    * [Lesson 9 : Working with RFID Module of PiCoder](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-9---working-with-rfid-module-of-picoder)
    * [Lesson 10 : Create Amazing Visuals with 8x8 LED MATRIX](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-10---create-amazing-visuals-with-8x8-led-matrix)
    * [Lesson 11 : Working with 3.2" Touch LCD of PiCoder](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-11---working-with-32-touch-lcd-of-picoder)
    * [Lesson 12 : Display Image on PiCoder](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#lesson-12---display-image-on-picoder)
 4. [Resources](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#resources)
 5. [Related HAT Products](https://github.com/sbcshop/PiCoder-Software/tree/main?tab=readme-ov-file#related-hat-products)


## Pinout 
<img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_pinout.jpg">
<img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/pinout_text.png" width="693" height="161">

## Getting Started with PiCoder  
### 1. How to Install Boot Firmware in Pico W of PiCoder kit

- Mostly, Picoder will be provided with firmware pre-installed, so you can skip this step if firmware is already present and directly jump start programming by following the below Step 2.
- How to know whether firmware is already present in your PiCoder: for this, just connect your PiCoder to your laptop, and if no extra device is detected, that means your PiCoder has it.
- And if you connect the PiCoder to a laptop without pressing the boot button, if it shows mass storage device named as "RPI-RP2" like the one below, then the firmware is not installed.
  
   <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- In this case, you need to add **MicroPython firmware** in PiCoder. First, you need to *Press and Hold* the boot button on pico W of PiCoder, and then, without releasing the button, connect it to PC/laptop using micro USB cable. Check below image for reference,
  
  <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif">

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the MicroPython firmware file provided in this repo above as ["PiCoder_firmware.uf2"](https://github.com/sbcshop/PiCoder-Software/blob/main/PiCoder_firmware.uf2)
or to download the latest firmware file from the official site, [visit here](https://micropython.org/download/rp2-pico-w/)     
     
- Drag and drop the MicroPython UF2 - ["PiCoder_firmware.uf2"](https://github.com/sbcshop/PiCoder-Software/blob/main/PiCoder_firmware.uf2) file provided in this github onto the RPI-RP2 volume. Your Pico W will reboot. You are now running MicroPython on PiCoder.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/firmware_installation.gif" />


### 2. Running First Program in PiCoder
- Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS of PC/laptop and install into your system.

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/thonny_IDE.png" width="463" height="388">

- Once done start **Thonny IDE application**, connect PiCoder kit with laptop/PC using micro usb cable.
  
- Download complete PiCoder software github and extract, so you can try example demo codes which is provided.

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/download_picoder_github.png" width="342" height="239">
  
- Open any one example in Thonny IDE. Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/img1_boardselect.png">
  
  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/img2_boardselect.png"> 

- If everything ok then you will get success message like as shown in below image, 
  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/Picoder_pico_connected.png">

- Before trying any example script make sure you have _**picoder.py**_ lib file present in PiCoder. If not, proceed to [step 3](https://github.com/sbcshop/PiCoder-Software/tree/main#3-how-to-move-script-codes-or-any-files-to-picoder) to move the file within PiCoder's Pico.
  
- With Demo LED Blink code open in IDE, click on Green Play Button or F5 to run script code. 
  
  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/run_demo_script.png">

- This is solely useful for testing code before moving it to PiCoder. However, in order to run the script without an IDE, you must first move it to PiCoder. To accomplish this, proceed to [step 3](https://github.com/sbcshop/PiCoder-Software/tree/main#3-how-to-move-script-codes-or-any-files-to-picoder) below.
  
### 3. How to Move Script Codes or Any Files to PiCoder

- Check that the file view is selected in Thonny IDE; if not, go to View > Files. This makes the computer and Pico folders visible.

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/fileview_step.gif">

- Open code script you want to move, click File > Save a Copy > Select Raspberry. Now name of code script must be main.py and select yes to overwrite previous.

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/filetransfer.gif">

- While moving lib file don't rename, maintain original name picoder.py, alternative file transfer method if renaming is not necessary->

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/otherway_filetransfer.gif">

  
  
## Lessons
Save whatever example code file you want to try as _**main.py**_ to Pico/ Pico W of PiCoder as shown in above steps, also make sure you added **[picoder.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/picoder.py)** lib file with default name. In [example](https://github.com/sbcshop/PiCoder-Software/tree/main/examples) folder you will find demo example script code to test onboard components of PiCoder. 

Checkout below lessons for each components and corresponding example links:

### Lesson 1 : How to Blink LED
**Objective:** In this chapter we will try to blink onboard LED using Pico W of PiCoder. There are two leds available.

**Hardware Connection:**
- Make sure you have put the jumper shown below, 

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_LED_connect.png">

  | Pico W | LED|
  |---|---|
  | GP14 | LED1 |
  | GP28 | LED2 |

- Software code will use:
  - Library => [**_picoder.py_**](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/picoder.py)
  - Class  => [**LED**](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#1-led)
  - Methods => _on, off_

- Example code: [Demo_LED.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_LED.py)

- Open code in Thonny IDE, select Raspberry Pi Pico board with proper COM port.

  <img src = "https://github.com/sbcshop/PiCoder-Software/blob/main/images/interface_window.png">

- Click Green play button to run directly and make sure to transfer **picoder.py** library in PiCoder's Pico.
- For standalone save this Demo_LED.py code into PiCoder's Pico as **main.py**. Now, whenever power up you will see LED starts blinking.


### Lesson 2 : How to play Buzzer of PiCoder
**Objective:** In this chapter we will learn to play onboard Buzzer of PiCoder.

**Hardware Connection:**
- Make sure you have put the jumper shown below, 

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_buzzer_connect.png">

  | Pico W | BUZZER |
  |---|---|
  | GP22 | BUZ |

- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **BUZZER**
  - Methods => _on, off_

- Example code: [Demo_Buzzer.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Buzzer.py)

- Open code in Thonny IDE, select board with proper COM port.
- Click Green play button to run directly and make sure to transfer **picoder.py** library in PiCoder's Pico.
- For standalone save this **Demo_Buzzer.py** code into PiCoder's Pico as **main.py**. Now, whenever you power up board you will see buzzer beeps in regular interval.

Related Examples:
 - [Buzzer Tone](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_BuzzerTone.py) : Create sound by changing frequency and intensity 
 

### Lesson 3 : Read value of POT 
**Objective:** Here we will learn about various methods for reading the value of the PiCoder's onboard potentiometer.

**Hardware Connection:**
- Make sure you have put the jumper shown below, 

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_POT_connect.png">

  | Pico W | POT |
  |---|---|
  | GP27 | ADC1 |

- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **POT**
  - Methods => _readPercent, readRaw_

- Example code: [Demo_POT.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_POT.py)
- Run code in Thonny IDE, and rotate POT to see change in value presented on shell terminal
  

### Lesson 4 : How to rotate Servo motor  
**Objective:** This lesson gives idea how you can easily rotate servo motor shaft with some angle 0-180 degree.

**Hardware Connection:**
- Make sure you have put the jumper shown below, 

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_servo_connect.png" width="130" height="239">

  | Pico W | SERVO |
  |---|---|
  | GP15 | SIG |

- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **SERVO**
  - Methods => _move, servo_Map_

- Example code: [Demo_Servo.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Servo.py)
- Checkout also example to control Servo using POT : [Demo_Servo_POT.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Servo_POT.py)


### Lesson 5 : How to Check Status of Button  
**Objective:** We will learn how to read status of Button if pressed or Not.

**Hardware Connection:**
- Make sure you have put the jumper shown below, 

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_buttons_connect.png">

  | Pico W | BUTTON |
  |---|---|
  | GP0 | BT1 |
  | GP4 | BT2 |
  | GP6 | BT3 |
  | GP19 | BT4 |

- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **BUTTON**
  - Methods => _read_

- Example code: [Demo_Button.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Button.py)
- Open and Run code in Thonny IDE, press button to see status change.
- Turn on and off LED using Button example : [Demo_Button_Combine.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Button_Combine.py)

### Lesson 6 : How to Read LDR Sensor for Light Detection 
**Objective:** We will learn how to read onboard LDR sensor value of PiCoder.

**Hardware Connection:**
- Make sure you have put the jumper shown below, 

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_ldr_connect.png">

  | Pico W | LDR |
  |---|---|
  | GP26 | ADC0 |
 
- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **LDR**
  - Methods => _read, readPercent_

- Example code: [Demo_LDR.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_LDR.py)
- Open and run code in Thonny IDE, change room light condition to see variation in LDR value 

### Lesson 7 :  How to read BME280 sensor of PiCoder
**Objective:** This lesson guides how to use BME280 for getting Temperature, pressure and relative humidity.

**Hardware Connection:**
- Make sure you have put the jumper shown below, 

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_bme280_connect.png">

  | Pico W | BME280 |
  |---|---|
  | GP20 | SDA |
  | GP21 | SCL |
 
- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **BME280**
  - Methods => _temperature, pressure, humidity_

- Example code: [Demo_BME280.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_BME280.py)
- Open and run code in Thonny IDE, you will get current room temperature, pressure and relative humidity value in terminal


### Lesson 8 : How to use Ultrasonic Sensor of PiCoder 
**Objective:** Here you will learn to know distance of object using Ultrasonic sensor. You can get value either in cm or inch.

**Hardware Connection:**
- Make sure you have put the jumper shown below,
 
  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_ultrasonic_connect.png" width="350" height="181">

  | Pico W | ULTRASONIC SENSOR |
  |---|---|
  | GP17 | ECHO |
  | GP16 | TRIG |
  
- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **ULTRASONIC**
  - Methods => _read, read_in_

- Example code: [Demo_UltrasonicSensor.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_UltrasonicSensor.py)
- Open and run code in Thonny IDE, move some object infront of Ultrasonic sensor to get distance value of object.

  
### Lesson 9 :  Working with RFID Module of PiCoder
**Objective:** This lesson demonstrates how to scan and read 125KHz RFID Card value using onboard RFID module of PiCoder.

**Hardware Connection:**
- Make sure you have put the jumper shown below,

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_rfid_connect.png" width="372" height="227">

  | Pico W | RFID |
  |---|---|
  | GP5 | RFID_TX |
  
- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **RFID**
  - Methods => _read_

- Example code: [Demo_RFID_module.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_RFID_module.py)
- Open and run code in Thonny IDE. Now bring any RFID card around module to read it.
- Scan status is indicated by LED, audio alert issued using Buzzer and RFID card value printed on terminal

### Lesson 10 :  Create amazing visuals with 8x8 LED MATRIX
**Objective:** Learn to generate colourful LED patterns on 8x8 LED MATRIX. 

**Hardware Connection:**
- Make sure you have put the jumper shown below,

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_ledmatrix_connect.png" width="309" height="246">

  | Pico W | 8X8 LED MATRIX |
  |---|---|
  | GP18 | RGB|
  
- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **LEDMATRIX**
  - Methods => _on, off, pixelon, pixeloff, chaser_

- Example code: [Demo_RGBLEDMatrix.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_RGBLEDMatrix.py)
- Open and run code in Thonny IDE to see various colour production and individual LED control
- Checkout this example how to create patterns : [RGBChaserPattern.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/RGBChaserPattern.py)


### Lesson 11 :  Working with 3.2" Touch LCD of PiCoder
**Objective:** This tutorial guides how to use 3.2" Touch LCD to create Interactive Visuals, generate graphics and see working of capacitive touch.

**Hardware Connection:**
- Make sure you have put the jumper shown below,
  
  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_display_connect.png" width="416" height="271">

  | Pico W | 3.2 Touch LCD |
  |---|---|
  | GP13 | BL |
  | GP12 | RST |
  | GP11 | DIN |
  | GP8 | D/C |
  | GP10 | CLK |
  | GP9 | CS |
  | GP2 | SDA |
  | GP3 | SCL |
  
- Software code will use:
  - Library => **_picoder.py_**
  - Class  => **LCD, TOUCH, RGB**
  - property => _touches, touched_
  - Methods => _getXY, draw_circle, fill_circle, clear, [more](https://github.com/sbcshop/PiCoder-Software/tree/main/documents#15-lcd)_
    
- Example code:
    - [Demo_LCD.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_LCD.py) : Demo how to present button response on display
    - [Demo_Graphics.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Graphics.py) : creates and display graphics on screen
    - [Demo_TOUCH.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_TOUCH.py) : Demo how to read touch co-ordinates 
    - [Demo_Touch&LCD.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Touch%26LCD.py) : Touch and Display combine operation

### Lesson 12 :  Display Image on PiCoder
**Objective:** Learn to display image file on PiCoder's screen.
- Follow same connection steps as shown in lesson 11
- Download [sample images](https://github.com/sbcshop/PiCoder-Software/tree/main/examples/Sample%20images) or if you want to convert your images then checkout guide to convert image file into raw image [here](https://github.com/sbcshop/PiCoder-Software/blob/main/documents/Step%20guide%20to%20convert%20img%20into%20raw%20file.pdf).
- Transfer image file to Pico of PiCoder and try below example code.

  <img src="https://github.com/sbcshop/PiCoder-Software/blob/main/images/img_transfer.gif">

- Example code: [Demo_imageDisplay.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_imageDisplay.py)



Detail Explanation of **picoder.py** Lib file is available **[here](https://github.com/sbcshop/PiCoder-Software/tree/main/documents)**.

Now you are ready to try out your own codes and build awesome projects with PiCoder, **_Happy Learning!_**

## Resources
  * [Schematic](https://github.com/sbcshop/PiCoder-Hardware/blob/main/Design%20Data/Sch%20PiCoder.pdf)
  * [Hardware Files](https://github.com/sbcshop/PiCoder-Hardware)
  * [Step File](https://github.com/sbcshop/PiCoder-Hardware/blob/main/Mechanical%20Data/PiCoder%20step.zip)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Getting Started with Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
  * [Getting Started with Pico W](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related HAT Products
 ![3vPicoRelayBoard](https://cdn.shopify.com/s/files/1/1217/2104/products/3vPicoRelayBoard.png?v=1617884866&width=200)
 
 * [2 Channel Relay Board](https://shop.sb-components.co.uk/products/pico-3v-relay-hat?_pos=1&_sid=82fa60545&_ss=r) - Compatible Relay Hat for PiCoder 
 
 ![1.14” LCD HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/6_c64376c7-a257-43a3-bb5f-0a9471741a7d.png?v=1624017126&width=200)
 
 * [1.14” LCD HAT](https://shop.sb-components.co.uk/products/1-14-lcd-hat-for-pico?_pos=3&_sid=82fa60545&_ss=r) - Compatible 1.14” LCD HAT for PiCoder 
 
 ![Motor Driver HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/motordriverforPico.png?v=1619523627&width=200)
 
 * [Motor Driver HAT](https://shop.sb-components.co.uk/products/pico-motor-driver?_pos=4&_sid=82fa60545&_ss=r) - Compatible 2 Channel Motor Driver HAT for PiCoder
 
 ![Ethernet_HAT](https://shop.sb-components.co.uk/cdn/shop/files/03_439625d0-e0d2-4555-b3b3-5d8fa316d7d8.jpg?v=1683535354&width=200)
 
 * [Ethernet HAT](https://shop.sb-components.co.uk/products/netpi-ethernet-hat-for-raspberry-pi-pico?_pos=2&_sid=82fa60545&_ss=r) - Compatible Ethernet HAT for PiCoder

 ![Barcode_Reader_HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/04.png?v=1669181209&width=200)
 
 * [Barcode Reader](https://shop.sb-components.co.uk/products/barcode-hat?_pos=5&_sid=82fa60545&_ss=r) - Compatible Barcode Reader HAT for PiCoder
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
