# PiCoder - Pico Learning Kit
100% DIY | 100% Programmable| L&D | RPi Pico | LED Matrix | LDR | 3.2" Touch LCD | BME280 | Ultrasonic Sensor | RFID | Dual USB | POT

A compact and comprehensive Raspberry Pi Pico W based Learning Kit having onboard actuators, sensors, and LEDs makes learning enjoyable.


<img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_banner.jpg">

The PiCoder is loaded with many features that are going to help you learn and explore many opportunities in the field of computer science and electronics.

PiCoder is an all-in-one STEM learning kit that allows students to work directly with the most common hardware components used in DIY projects. 
Features the most well-known Raspberry Pi Pico, which enjoys strong community support.The most popular programming languages, Micropython, Ciruitpython, and Arduino, are supported across platforms.

Because the lesson for the PiCoder kit is mostly based on Micropython, it is advised that you understand the very fundamentals of Python.
This GitHub provides details and step-by-step instructions how to use PiCoder kit. 

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

  
  
### Example Codes
Save whatever example code file you want to try as main.py to Pico/ Pico W of PiCoder as shown in above step, also make sure you added [picoder.py](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/picoder.py) lib file with default name. In [example](https://github.com/sbcshop/PiCoder-Software/tree/main/examples) folder you will find demo example script code to test onboard components of PiCoder like,

- [Buzzer](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_BuzzerTone.py) : code to test onboard Buzzer
- [RGB Matrix](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_RGBLEDMatrix.py) : Run this code to check various control and color production on 8x8 RGB MATRIX
- [Ultrasonic Sensor](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_UltrasonicSensor.py) : code to measure distance of object
- [Servo and POT](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Servo_POT.py) : rotate servo motor using POT
- [Combine Operation](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Button_Combine.py) : press button to see LED blink and Relay ON/OFF.
- [RGB LED Chaser](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/RGBChaserPattern.py) : Demo code to develop some LED chaser color pattern 
- [Touch Display](https://github.com/sbcshop/PiCoder-Software/blob/main/examples/Demo_Touch%26LCD.py) : Play with Touch Display 
- [and Many more...](https://github.com/sbcshop/PiCoder-Software/tree/main/examples)
   

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
