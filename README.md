# PiCoder - Pico Learning Kit
100% DIY | 100% Programmable| L&D | RPi Pico | LED Matrix | LDR | 3.2" Touch LCD | BME280 | Ultrasonic Sensor | RFID | Dual USB | POT

A compact and comprehensive Raspberry Pi Pico W based Learning Kit having onboard actuators, sensors, and LEDs makes learning enjoyable.


<img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_kits.png"/>

The PiCoder is loaded with many features that are going to help you learn and explore many opportunities in the field of computer science and electronics.

## Getting Started with PiCoder  
### 1. How to install boot Firmware in PiCoder kit

- Mostly, Picoder will be shipped with firmware pre-installed, so you can skip this step if firmware is already present and directly jump start programming by following the below Step 2.
- How to know whether firmware is already present in your PiCoder: for this, just connect your PiCoder to your laptop, and if no extra device is detected, that means your PiCoder has it.
- And if you connect the PiCoder to a laptop without pressing the boot button, if it shows a folder named "RPI-RP2" like the one below, then the firmware is not installed.
  
   <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- In this case, you need to add **MicroPython firmware** in PiCoder. First,  you need to *Press and Hold* the boot button on PiCoder, and then, without releasing the button, connect it to the USB port of your PC/laptop. 
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/picoder_boot_mode.gif" />

- Now your device is in boot mode, and you will see a new device named "RPI-RP2" as shown in the below figure.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the MicroPython firmware file provided in this repo above as ["firmware.uf2"](https://github.com/sbcshop/PiCoder-Software/blob/main/firmware.uf2)
or to download the latest firmware file from the official site, [visit here](https://micropython.org/download/rp2-pico-w/)     
     
- Just copy and paste the firmware into the RPI-RP2 folder, and now the bootloader is properly installed inside the PiCoder. To verify remove device and re-insert into PC/Laptop, no need to press boot button. This time you will see a new device as RPI-RP2.


### 2. Running First Program in PiCoder
- Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and installed.

- Once done start **Thonny IDE application**,
  - Connect PiCoder kit with laptop/PC using micro usb cable
  
  - After this go to Run -> Configure interpreter, choose device and suitable com port as shown in below images
    <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/img1.jpg" />
    <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/img2.jpg" />
    <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/img3.jpg" />
    
   - There is other option to select device at bottom right side as shown in below figure
     <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/img4.jpg" />
   
   - Write simple python code and click on green run button to make your script running on PiCoder
     <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/img5.jpg" />
    

Now you are ready to try out your own codes, **_Happy Coding!_**

## Related Projects

## Documentation
  * [MicroPython getting started for RPI](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related HAT Products
 ![3vPicoRelayBoard](https://cdn.shopify.com/s/files/1/1217/2104/products/3vPicoRelayBoard.png?v=1617884866&width=200)
 
 * [2 Channel Relay Board](https://shop.sb-components.co.uk/products/pico-3v-relay-hat?_pos=1&_sid=82fa60545&_ss=r) - Compatible Relay Hat for PiCoder 
 
 ![1.14” LCD HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/6_c64376c7-a257-43a3-bb5f-0a9471741a7d.png?v=1624017126&width=200)
 
 * [1.14” LCD HAT](https://shop.sb-components.co.uk/products/1-14-lcd-hat-for-pico?_pos=3&_sid=82fa60545&_ss=r) - Compatible 1.14” LCD HAT for PiCoder 
 
 ![Motor Driver HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/motordriverforPico.png?v=1619523627&width=200)
 
 * [Motor Driver HAT](https://shop.sb-components.co.uk/products/pico-motor-driver?_pos=4&_sid=82fa60545&_ss=r) - Compatible 2 Channel Motor Driver HAT for PiCoder
 
 ![Ethernet_HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/NetPi_4.png?v=1675947155&width=200)
 
 * [Ethernet HAT](https://shop.sb-components.co.uk/products/netpi-ethernet-hat-for-raspberry-pi-pico?_pos=2&_sid=82fa60545&_ss=r) - Compatible Ethernet HAT for PiCoder

 ![Barcode_Reader_HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/04.png?v=1669181209&width=200)
 
 * [Barcode Reader](https://shop.sb-components.co.uk/products/barcode-hat?_pos=5&_sid=82fa60545&_ss=r) - Compatible Barcode Reader HAT for PiCoder
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
