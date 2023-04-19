# PiCoder
100% DIY | 100% Programmable| LED | RPi Pico | LED Matrix | LDR | 3.2" Touch LCD | BME280 | Ultrasonic Sensor | RFID | Dual USB | POT

A compact and comprehensive Raspberry Pi Pico W based Learning Kit having onboard actuators, sensors, and LEDs makes learning enjoyable.

## Getting Started with PiCoder  
### 1. How to install boot Firmware in PiCoder

- Mostly, Picoder will be shipped with firmware pre-installed, so you can skip this step if firmware is already present and directly jump start programming by following the below Step 2.
- How to know whether firmware is already present in your PiCoder: for this, just connect your PiCoder to your laptop, and if no extra device is detected, that means your PiCoder has it.
- And if you connect the PiCoder to a laptop without pressing the boot button, if it shows a folder named "RPI-RP2" like the one below, then the firmware is not installed.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" />

- In this case, you need to add **MicroPython firmware** in PiCoder. First,  you need to *Press and Hold* the boot button on PiCoder, and then, without releasing the button, connect it to the USB port of your PC/laptop. 
  <img src= "https://github.com/sbcshop/HackyPi-Software/blob/main/images/HackyPi_bootloader_install.gif" />

- Now your device is in boot mode, and you will see a new device named "RPI-RP2" as shown in the below figure.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" />

- Download the MicroPython firmware file provided in this repo above as ["firmware.uf2"](https://github.com/sbcshop/HackyPi-Software/blob/main/firmware.uf2)
or to download the latest firmware file from the official site, [visit here](https://micropython.org/download/rp2-pico-w/)     
     
- Just copy and paste the firmware into the RPI-RP2 folder, and now the bootloader is properly installed inside the PiCoder. To verify remove device and re-insert into PC/Laptop, no need to press boot button. This time you will see a new device as RPI-RP2.
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />


### 2. Running First Program in PiCoder
- Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and installed.

- Once done start **Thonny IDE application**, after this go to run->select interpreter, choose device and suitable com port
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />
    
- Write simple python code and click on green run button
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img20.png" />
    <img src= "https://github.com/sbcshop/HackyPi-Software/blob/main/images/sample_hello_program.png" />

Now you are ready to try out your own codes, **Happy Coding!**

## Documentation

* [PiCoder Hardware]() 
* [PiCoder Schematic]() 
* [MicroPython getting started for RPI](https://docs.micropython.org/en/latest/rp2/quickref.html)
* [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related HAT Products
 ![SquaryFi](https://cdn.shopify.com/s/files/1/1217/2104/products/2_12d19ffa-bcda-47bf-8ea9-bb76fc40aee3.png?v=1670307456&width=300)
 
 * [Roundy](https://shop.sb-components.co.uk/products/roundy?variant=39785171681363) - 1.28" Round LCD version based on ESP8266 and RP2040
 
 ![Roundy](https://cdn.shopify.com/s/files/1/1217/2104/products/roundypi.png?v=1650457581&width=300)

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
