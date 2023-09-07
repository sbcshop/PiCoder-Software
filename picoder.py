"""PiCoder Library Module. """
from machine import Pin, ADC, PWM, UART, I2C,SPI
from math import cos, sin, pi, radians
from sys import implementation
from framebuf import FrameBuffer, RGB565  # type: ignore
import ustruct  # type: ignore
from neopixel import NeoPixel
import time,utime
from time import sleep
from micropython import const

# imports
try:
    import struct
except ImportError:
    import ustruct as struct
    
    
# BME280 default address.
BME280_I2CADDR = 0x76

# Operating Modes
BME280_OSAMPLE_1 = 1
BME280_OSAMPLE_2 = 2
BME280_OSAMPLE_4 = 3
BME280_OSAMPLE_8 = 4
BME280_OSAMPLE_16 = 5

# BME280 Registers
BME280_REGISTER_DIG_T1 = 0x88  # Trimming parameter registers
BME280_REGISTER_DIG_T2 = 0x8A
BME280_REGISTER_DIG_T3 = 0x8C

BME280_REGISTER_DIG_P1 = 0x8E
BME280_REGISTER_DIG_P2 = 0x90
BME280_REGISTER_DIG_P3 = 0x92
BME280_REGISTER_DIG_P4 = 0x94
BME280_REGISTER_DIG_P5 = 0x96
BME280_REGISTER_DIG_P6 = 0x98
BME280_REGISTER_DIG_P7 = 0x9A
BME280_REGISTER_DIG_P8 = 0x9C
BME280_REGISTER_DIG_P9 = 0x9E

BME280_REGISTER_DIG_H1 = 0xA1
BME280_REGISTER_DIG_H2 = 0xE1
BME280_REGISTER_DIG_H3 = 0xE3
BME280_REGISTER_DIG_H4 = 0xE4
BME280_REGISTER_DIG_H5 = 0xE5
BME280_REGISTER_DIG_H6 = 0xE6
BME280_REGISTER_DIG_H7 = 0xE7

BME280_REGISTER_CHIPID = 0xD0
BME280_REGISTER_VERSION = 0xD1
BME280_REGISTER_SOFTRESET = 0xE0

BME280_REGISTER_CONTROL_HUM = 0xF2
BME280_REGISTER_CONTROL = 0xF4
BME280_REGISTER_CONFIG = 0xF5
BME280_REGISTER_PRESSURE_DATA = 0xF7
BME280_REGISTER_TEMP_DATA = 0xFA
BME280_REGISTER_HUMIDITY_DATA = 0xFD

#default address for i2c Touch
_FT6206_DEFAULT_I2C_ADDR = 0x38

# FT6236 Registers
_FT6XXX_REG_DATA = const(0x00)
_FT6XXX_REG_NUMTOUCHES = const(0x02)
_FT6XXX_REG_THRESHHOLD = const(0x80)
_FT6XXX_REG_POINTRATE = const(0x88)
_FT6XXX_REG_LIBH = const(0xA1)
_FT6XXX_REG_LIBL = const(0xA2)
_FT6XXX_REG_CHIPID = const(0xA3)
_FT6XXX_REG_FIRMVERS = const(0xA6)
_FT6XXX_REG_VENDID = const(0xA8)
_FT6XXX_REG_RELEASE = const(0xAF)


#class to control onboard LED of PiCoder
class LED():
    def __init__(self, led_pin_number):
        if led_pin_number == 1:
            self.led_pin = Pin(14, Pin.OUT)
        elif led_pin_number == 2:
            self.led_pin = Pin(28, Pin.OUT)
        else :
            self.led_pin = Pin(led_pin_number, Pin.OUT)
        
    def on(self):
        self.led_pin.on()
    
    def off(self):
        self.led_pin.off()
        
# class to control onboard Relay        
class RELAY():
    def __init__(self, relay_pin_number):
        if relay_pin_number == 1:
            self.relay_pin = Pin(7, Pin.OUT)
        elif relay_pin_number == 2:
            self.relay_pin = Pin(1, Pin.OUT)
    
    def on(self):
        self.relay_pin.on()
    
    def off(self):
        self.relay_pin.off()   

# class to control Buzzer
class BUZZER():
    def __init__(self):
        self.buzzer_pin = Pin(22, Pin.OUT)
          
    def on(self):	#function to Turn ON Buzzer
        self.buzzer_pin.on()
    
    def off(self):	#function to Turn OFF Buzzer
        self.buzzer_pin.off()

# class to control Buzzer
class BUZZERTONE():
    def __init__(self):
        self.buzzer_pwm = PWM(Pin(22))
        
    def play(self,frequency=512,duty=5000): # function to play tone on buzzer with define frequency
        self.buzzer_pwm.duty_u16(duty)  # HIGH will sound buzzer
        self.buzzer_pwm.freq(frequency)

    def stop(self):	# Function to stop buzzer
        self.buzzer_pwm.duty_u16(0) # Low will stop buzzer

 
# class to read Picoder onboard Buttons value 
class BUTTON():
    def __init__(self, button_pin_number):
        """Initialize BUTTON.

        Args:
            button_pin_number (int):  1, 2, 3, 4 for onboard Buttons,
                                      and pass GPIOs number for interfacing external buttons
            
        """
        if button_pin_number == 1:
            self.button_pin = Pin(0, Pin.IN) #input mode setup for read operation 
        elif button_pin_number == 2:
            self.button_pin = Pin(4, Pin.IN)
        elif button_pin_number == 3:
            self.button_pin = Pin(6, Pin.IN)
        elif button_pin_number == 4:
            self.button_pin = Pin(19, Pin.IN)
        else :
            self.button_pin = Pin(button_pin_number, Pin.IN) 
            
    def read(self):
        """ provides button status value
            -> 0 (for Not Pressed)
            -> 1 (for Pressed)
        """
        return self.button_pin.value()

# class to read potentiometer value as Raw, or in Percentage
class POT():
    def __init__(self,pot_pin_number = 1):
        """Initialize POT.

        Args:
            pot_pin_number (Optional int):  default is 1 for onboard POT at GPIO27/ADC1,
                                            0 (GPIO26/ADC0), 2 (GPIO28/ADC2). 
        """
        
        self.adc = ADC(pot_pin_number) 
        
    def read(self):
        """ returns Analog value at GPIO for corresponding Potentiometer Knob movement
        """
        return self.adc.read_u16()  # read raw analog value in 0-65535 across voltage range 0.0v - 3.3v
    
    def readPercent(self):		
        """calculate and returns Potentiometer value in Percentage 0-100%
        """
        pot_Value = self.adc.read_u16()
        potVal_Percent = round(pot_Value/65535*100)
        return potVal_Percent

# class to read LDR value as Raw, or in Percentage
class LDR():
    def __init__(self,ldr_pin_number = 0):
        """Initialize LDR.

        Args:
            ldr_pin_number (Optional int):  default is 0 for onboard LDR at GPIO26/ADC0,
                                            1 (GPIO26/ADC1), 2 (GPIO28/ADC2). 
        """
        
        self.adc = ADC(ldr_pin_number) 
        
    def read(self):
        """ returns Analog value of LDR 
        """
        return self.adc.read_u16()  # read raw analog value in 0-65535 across voltage range 0.0v - 3.3v
    
    def readPercent(self):		
        """calculate and returns LDR value in Percentage 0-100%
        """
        ldr_Value = self.adc.read_u16()
        ldrVal_Percent = round(ldr_Value/65535*100)
        return ldrVal_Percent

class ULTRASONIC:
    def __init__(self,echoPin = 17, trigPin = 16):
        """Initialize ULTRASONIC.

        Args:
            echoPin (Optional int): default GPIO17
            trigPin (Optional int): default GPIO16 
            
        """   
        self.echoPin = Pin(echoPin, Pin.IN)
        self.trigPin = Pin(trigPin, Pin.OUT)
    
    def read(self):
        """ returns distance value in cm 
        """
        #create pulse
        self.trigPin.low()
        utime.sleep_us(2)
        self.trigPin.high()
        utime.sleep_us(5)
        self.trigPin.low()
        
        #calculate sound travel time
        while self.echoPin.value() == 0:
            #print(self.echoPin.value())
            tOFF = utime.ticks_us()
        while self.echoPin.value() == 1:
            #print(self.echoPin.value())
            tON = utime.ticks_us()   
        timepassed = tON - tOFF
        
        #calculate distance from time
        distance_cm = round((timepassed * 0.0343) / 2,2)

        return distance_cm
    
    def read_in(self):		
        """returns distance value in inch
        """
        distance_in = self.read() / 2.54
        
        return round(distance_in,2)
    
    
class SERVO:
    """ A simple class for controlling a 9g servo with the Raspberry Pi Pico.
 
    Attributes:
 
        minVal: An integer denoting the minimum duty value for the servo motor.
 
        maxVal: An integer denoting the maximum duty value for the servo motor.
 
    """
 
    def __init__(self, pin=15, minVal=2500, maxVal=7500):
        """ Creates a new Servo Object.
 
        args:
 
            pin (int): integer denoting the number of the GPIO pin
 
            minVal (int): Optional, denotes the minimum duty value to be used for this servo.
 
            maxVal (int): Optional, denotes the maximum duty value to be used for this servo.
 
        """
        pin = Pin(pin, Pin.OUT) #set mode as OUTPUT
        self.__pwm = PWM(pin)	#create PWM instance
        self.__pwm.freq(50)		
        self.minVal = minVal
        self.maxVal = maxVal
 
    def deinit(self):
        """ Deinitializes the underlying PWM object.
 
        """
        self.__pwm.deinit()
 
    def goto(self, value: int):
        """ Moves the servo to the specified position.
 
        args:
 
            value (int): The position to move to, represented by a value from 0 to 1024 (inclusive).
 
        """
        if value < 0:
            value = 0
        if value > 1024:
            value = 1024
        delta = self.maxVal-self.minVal
        target = int(self.minVal + ((value / 1024) * delta))
        self.__pwm.duty_u16(target)
 
    def middle(self):
        """ Moves the servo to the middle.
        """
        self.goto(512)
 
    def free(self):
        """ Allows the servo to be moved freely.
        """
        self.__pwm.duty_u16(0)
        
    def servo_Map(self,x, in_min, in_max, out_min, out_max):
        """ Mapping 0 - 180 range into 0 - 1024
        """
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
     
    def move(self,angle: int):
        """ takes angle value to move servo at
        """
        if angle < 0:
            angle = 0
        if angle > 180:
            angle = 180
        self.goto(round(self.servo_Map(angle,0,180,0,1024))) # mapping 0-180 into 0-1024 then moving at angle 

class RFID:
    def __init__(self,RFID_pin=5, byteNumber=12):
        """Initialize RFID.

        Args:
            RFID_pin (Optional int): default GPIO5
            byteNumber (Optional int): default 12 byte, decides number of bytes to read
        """
        self.uart = UART(1, baudrate=9600,rx=Pin(RFID_pin),bits=8, parity=None, stop=1)
        self.byteNumber = byteNumber
        
    def read(self):
        """ returns utf-8 format of RFID card value
        """
        utf = self.uart.read(self.byteNumber)
        if utf: 
            return utf.decode("utf-8")
    
    def readRaw(self):
        """ returns raw RFID card value
        """
        return self.uart.read(self.byteNumber)

class LEDMATRIX:
    def __init__(self, led_count = 64, matrix_pin=18 ):
        """Initialize 8x8 RGB LED MATRIX.

        Args:
            led_count (Optional int): default 64 LEDs onboard of PiCoder
            rgb_led_pin (Optional int): default GPIO18 for PiCoder RGB LED Matrix connection
        """
       # Define the number of LEDs and the GPIO pin connected
        self.led_count = led_count 
        self.matrix_pin = Pin(matrix_pin, Pin.OUT) # set GPIO as output to drive NeoPixels
        self.np = NeoPixel(self.matrix_pin, self.led_count )   # create NeoPixel driver
        
    # Function to adjust brightness of a color
    def adjust_brightness(self, color, brightness):
        r, g, b = color
        r = int(r * brightness)
        g = int(g * brightness)
        b = int(b * brightness)
        return r, g, b
        
    def pixelon(self, ledpos, color=(255, 255, 255), brightness=0.5):
        self.np[ledpos] = self.adjust_brightness(color,brightness)
        self.np.write()   # write data to all pixels
    
    def pixeloff(self, ledpos):
        self.np[ledpos] = (0, 0, 0)
        self.np.write()   # write data to all pixels
    
    def on(self,color=(255, 255, 255), brightness=0.5):
        for i in range(self.led_count):
            self.pixelon(i,color,brightness)
    
    def off(self):
        for i in range(self.led_count):
            self.pixeloff(i)
                
    def readpixel(self,ledpos):
        r, g, b = self.np[ledpos]     # get pixel colour
        return r, g, b
    
    def chaser(self,startpos=0, endpos=64, delay=0.1, color=(255,255,255), brightness=0.2):
        for i in range(startpos,endpos):
            self.pixelon(i, color, brightness) 
            sleep(delay)
            
        for i in reversed(range(startpos, endpos)):
            self.pixeloff(i)
            sleep(delay)
            
class Device:
  """Class for communicating with an I2C device.

  Allows reading and writing 8-bit, 16-bit, and byte array values to
  registers on the device."""

  def __init__(self, address, i2c):
    """Create an instance of the I2C device at the specified address using
    the specified I2C interface object."""
    self._address = address
    self._i2c = i2c

  def writeRaw8(self, value):
    """Write an 8-bit value on the bus (without register)."""
    value = value & 0xFF
    self._i2c.writeto(self._address, value)

  def write8(self, register, value):
    """Write an 8-bit value to the specified register."""
    b=bytearray(1)
    b[0]=value & 0xFF
    self._i2c.writeto_mem(self._address, register, b)

  def write16(self, register, value):
    """Write a 16-bit value to the specified register."""
    value = value & 0xFFFF
    b=bytearray(2)
    b[0]= value & 0xFF
    b[1]= (value>>8) & 0xFF
    self.i2c.writeto_mem(self._address, register, value)

  def readRaw8(self):
    """Read an 8-bit value on the bus (without register)."""
    return int.from_bytes(self._i2c.readfrom(self._address, 1),'little') & 0xFF

  def readU8(self, register):
    """Read an unsigned byte from the specified register."""
    return int.from_bytes(
        self._i2c.readfrom_mem(self._address, register, 1),'little') & 0xFF

  def readS8(self, register):
    """Read a signed byte from the specified register."""
    result = self.readU8(register)
    if result > 127:
      result -= 256
    return result

  def readU16(self, register, little_endian=True):
    """Read an unsigned 16-bit value from the specified register, with the
    specified endianness (default little endian, or least significant byte
    first)."""
    result = int.from_bytes(
        self._i2c.readfrom_mem(self._address, register, 2),'little') & 0xFFFF
    if not little_endian:
      result = ((result << 8) & 0xFF00) + (result >> 8)
    return result

  def readS16(self, register, little_endian=True):
    """Read a signed 16-bit value from the specified register, with the
    specified endianness (default little endian, or least significant byte
    first)."""
    result = self.readU16(register, little_endian)
    if result > 32767:
      result -= 65536
    return result

  def readU16LE(self, register):
    """Read an unsigned 16-bit value from the specified register, in little
    endian byte order."""
    return self.readU16(register, little_endian=True)

  def readU16BE(self, register):
    """Read an unsigned 16-bit value from the specified register, in big
    endian byte order."""
    return self.readU16(register, little_endian=False)

  def readS16LE(self, register):
    """Read a signed 16-bit value from the specified register, in little
    endian byte order."""
    return self.readS16(register, little_endian=True)

  def readS16BE(self, register):
    """Read a signed 16-bit value from the specified register, in big
    endian byte order."""
    return self.readS16(register, little_endian=False)



class BME280_BASE:
  def __init__(self, mode=BME280_OSAMPLE_1, address=BME280_I2CADDR, i2c=None,
               **kwargs):
    # Check that mode is valid.
    if mode not in [BME280_OSAMPLE_1, BME280_OSAMPLE_2, BME280_OSAMPLE_4,
                    BME280_OSAMPLE_8, BME280_OSAMPLE_16]:
        raise ValueError(
            'Unexpected mode value {0}. Set mode to one of '
            'BME280_ULTRALOWPOWER, BME280_STANDARD, BME280_HIGHRES, or '
            'BME280_ULTRAHIGHRES'.format(mode))
    self._mode = mode
    # Create I2C device.
    if i2c is None:
      raise ValueError('An I2C object is required.')
    self._device = Device(address, i2c)
    # Load calibration values.
    self._load_calibration()
    self._device.write8(BME280_REGISTER_CONTROL, 0x3F)
    self.t_fine = 0

  def _load_calibration(self):

    self.dig_T1 = self._device.readU16LE(BME280_REGISTER_DIG_T1)
    self.dig_T2 = self._device.readS16LE(BME280_REGISTER_DIG_T2)
    self.dig_T3 = self._device.readS16LE(BME280_REGISTER_DIG_T3)

    self.dig_P1 = self._device.readU16LE(BME280_REGISTER_DIG_P1)
    self.dig_P2 = self._device.readS16LE(BME280_REGISTER_DIG_P2)
    self.dig_P3 = self._device.readS16LE(BME280_REGISTER_DIG_P3)
    self.dig_P4 = self._device.readS16LE(BME280_REGISTER_DIG_P4)
    self.dig_P5 = self._device.readS16LE(BME280_REGISTER_DIG_P5)
    self.dig_P6 = self._device.readS16LE(BME280_REGISTER_DIG_P6)
    self.dig_P7 = self._device.readS16LE(BME280_REGISTER_DIG_P7)
    self.dig_P8 = self._device.readS16LE(BME280_REGISTER_DIG_P8)
    self.dig_P9 = self._device.readS16LE(BME280_REGISTER_DIG_P9)

    self.dig_H1 = self._device.readU8(BME280_REGISTER_DIG_H1)
    self.dig_H2 = self._device.readS16LE(BME280_REGISTER_DIG_H2)
    self.dig_H3 = self._device.readU8(BME280_REGISTER_DIG_H3)
    self.dig_H6 = self._device.readS8(BME280_REGISTER_DIG_H7)

    h4 = self._device.readS8(BME280_REGISTER_DIG_H4)
    h4 = (h4 << 24) >> 20
    self.dig_H4 = h4 | (self._device.readU8(BME280_REGISTER_DIG_H5) & 0x0F)

    h5 = self._device.readS8(BME280_REGISTER_DIG_H6)
    h5 = (h5 << 24) >> 20
    self.dig_H5 = h5 | (
        self._device.readU8(BME280_REGISTER_DIG_H5) >> 4 & 0x0F)

  def read_raw_temp(self):
    """Reads the raw (uncompensated) temperature from the sensor."""
    meas = self._mode
    self._device.write8(BME280_REGISTER_CONTROL_HUM, meas)
    meas = self._mode << 5 | self._mode << 2 | 1
    self._device.write8(BME280_REGISTER_CONTROL, meas)
    sleep_time = 1250 + 2300 * (1 << self._mode)

    sleep_time = sleep_time + 2300 * (1 << self._mode) + 575
    sleep_time = sleep_time + 2300 * (1 << self._mode) + 575
    time.sleep_us(sleep_time)  # Wait the required time
    msb = self._device.readU8(BME280_REGISTER_TEMP_DATA)
    lsb = self._device.readU8(BME280_REGISTER_TEMP_DATA + 1)
    xlsb = self._device.readU8(BME280_REGISTER_TEMP_DATA + 2)
    raw = ((msb << 16) | (lsb << 8) | xlsb) >> 4
    return raw

  def read_raw_pressure(self):
    """Reads the raw (uncompensated) pressure level from the sensor."""
    """Assumes that the temperature has already been read """
    """i.e. that enough delay has been provided"""
    msb = self._device.readU8(BME280_REGISTER_PRESSURE_DATA)
    lsb = self._device.readU8(BME280_REGISTER_PRESSURE_DATA + 1)
    xlsb = self._device.readU8(BME280_REGISTER_PRESSURE_DATA + 2)
    raw = ((msb << 16) | (lsb << 8) | xlsb) >> 4
    return raw

  def read_raw_humidity(self):
    """Assumes that the temperature has already been read """
    """i.e. that enough delay has been provided"""
    msb = self._device.readU8(BME280_REGISTER_HUMIDITY_DATA)
    lsb = self._device.readU8(BME280_REGISTER_HUMIDITY_DATA + 1)
    raw = (msb << 8) | lsb
    return raw

  def read_temperature(self):
    """Get the compensated temperature in 0.01 of a degree celsius."""
    adc = self.read_raw_temp()
    var1 = ((adc >> 3) - (self.dig_T1 << 1)) * (self.dig_T2 >> 11)
    var2 = ((
        (((adc >> 4) - self.dig_T1) * ((adc >> 4) - self.dig_T1)) >> 12) *
        self.dig_T3) >> 14
    self.t_fine = var1 + var2
    return (self.t_fine * 5 + 128) >> 8

  def read_pressure(self):
    """Gets the compensated pressure in Pascals."""
    adc = self.read_raw_pressure()
    var1 = self.t_fine - 128000
    var2 = var1 * var1 * self.dig_P6
    var2 = var2 + ((var1 * self.dig_P5) << 17)
    var2 = var2 + (self.dig_P4 << 35)
    var1 = (((var1 * var1 * self.dig_P3) >> 8) +
            ((var1 * self.dig_P2) >> 12))
    var1 = (((1 << 47) + var1) * self.dig_P1) >> 33
    if var1 == 0:
      return 0
    p = 1048576 - adc
    p = (((p << 31) - var2) * 3125) // var1
    var1 = (self.dig_P9 * (p >> 13) * (p >> 13)) >> 25
    var2 = (self.dig_P8 * p) >> 19
    return ((p + var1 + var2) >> 8) + (self.dig_P7 << 4)

  def read_humidity(self):
    adc = self.read_raw_humidity()
    # print 'Raw humidity = {0:d}'.format (adc)
    h = self.t_fine - 76800
    h = (((((adc << 14) - (self.dig_H4 << 20) - (self.dig_H5 * h)) +
         16384) >> 15) * (((((((h * self.dig_H6) >> 10) * (((h *
                          self.dig_H3) >> 11) + 32768)) >> 10) + 2097152) *
                          self.dig_H2 + 8192) >> 14))
    h = h - (((((h >> 15) * (h >> 15)) >> 7) * self.dig_H1) >> 4)
    h = 0 if h < 0 else h
    h = 419430400 if h > 419430400 else h
    return h >> 12

  @property
  def temperature(self):
    "Return the temperature in degrees."
    t = self.read_temperature()
    ti = t // 100
    td = t - ti * 100
    return "{}.{:02d}C".format(ti, td)

  @property
  def pressure(self):
    "Return the temperature in hPa."
    p = self.read_pressure() // 256
    pi = p // 100
    pd = p - pi * 100
    return "{}.{:02d}".format(pi, pd)

  @property
  def humidity(self):
    "Return the humidity in percent."
    h = self.read_humidity()
    hi = h // 1024
    hd = h * 100 // 1024 - hi * 100
    return "{}.{:02d}%".format(hi, hd)

class BME280():
    def __init__(self, scl=21, sda=20 ):
        """Initialize BME280 Sensor.

        Args:
            scl (Optional int): default GPIO21 for PiCoder BME280 sensor
            sda (Optional int): default GPIO20 for PiCoder BME280 sensor
        """
        self.i2c = I2C(0,scl=Pin(21), sda=Pin(20), freq=40000)#all sensor connected through I2C

        self.bme = BME280_BASE(i2c=self.i2c) #pressure,temperature and humidity sensor
        
    def temperature(self):
        """ returns temperature value in degree
        """
        return self.bme.temperature
    
    def pressure(self):
        """ returns pressure value in hPa
        """
        return self.bme.pressure
    
    def humidity(self):
        """ returns humidity value in percentage
        """
        return self.bme.humidity



def RGB(r, g, b):
    """Return RGB565 color value.

    Args:
        r (int): Red value.
        g (int): Green value.
        b (int): Blue value.
    """
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3


class LCD(object):
    """Serial interface for 16-bit color (5-6-5 RGB) IL9341 display.

    Note:  All coordinates are zero based.
    """

    # Command constants from ILI9341 datasheet
    NOP = const(0x00)  # No-op
    SWRESET = const(0x01)  # Software reset
    RDDID = const(0x04)  # Read display ID info
    RDDST = const(0x09)  # Read display status
    SLPIN = const(0x10)  # Enter sleep mode
    SLPOUT = const(0x11)  # Exit sleep mode
    PTLON = const(0x12)  # Partial mode on
    NORON = const(0x13)  # Normal display mode on
    RDMODE = const(0x0A)  # Read display power mode
    RDMADCTL = const(0x0B)  # Read display MADCTL
    RDPIXFMT = const(0x0C)  # Read display pixel format
    RDIMGFMT = const(0x0D)  # Read display image format
    RDSELFDIAG = const(0x0F)  # Read display self-diagnostic
    INVOFF = const(0x20)  # Display inversion off
    INVON = const(0x21)  # Display inversion on
    GAMMASET = const(0x26)  # Gamma set
    DISPLAY_OFF = const(0x28)  # Display off
    DISPLAY_ON = const(0x29)  # Display on
    SET_COLUMN = const(0x2A)  # Column address set
    SET_PAGE = const(0x2B)  # Page address set
    WRITE_RAM = const(0x2C)  # Memory write
    READ_RAM = const(0x2E)  # Memory read
    PTLAR = const(0x30)  # Partial area
    VSCRDEF = const(0x33)  # Vertical scrolling definition
    MADCTL = const(0x36)  # Memory access control
    VSCRSADD = const(0x37)  # Vertical scrolling start address
    PIXFMT = const(0x3A)  # COLMOD: Pixel format set
    WRITE_DISPLAY_BRIGHTNESS = const(0x51)  # Brightness hardware dependent!
    READ_DISPLAY_BRIGHTNESS = const(0x52)
    WRITE_CTRL_DISPLAY = const(0x53)
    READ_CTRL_DISPLAY = const(0x54)
    WRITE_CABC = const(0x55)  # Write Content Adaptive Brightness Control
    READ_CABC = const(0x56)  # Read Content Adaptive Brightness Control
    WRITE_CABC_MINIMUM = const(0x5E)  # Write CABC Minimum Brightness
    READ_CABC_MINIMUM = const(0x5F)  # Read CABC Minimum Brightness
    FRMCTR1 = const(0xB1)  # Frame rate control (In normal mode/full colors)
    FRMCTR2 = const(0xB2)  # Frame rate control (In idle mode/8 colors)
    FRMCTR3 = const(0xB3)  # Frame rate control (In partial mode/full colors)
    INVCTR = const(0xB4)  # Display inversion control
    DFUNCTR = const(0xB6)  # Display function control
    PWCTR1 = const(0xC0)  # Power control 1
    PWCTR2 = const(0xC1)  # Power control 2
    PWCTRA = const(0xCB)  # Power control A
    PWCTRB = const(0xCF)  # Power control B
    VMCTR1 = const(0xC5)  # VCOM control 1
    VMCTR2 = const(0xC7)  # VCOM control 2
    RDID1 = const(0xDA)  # Read ID 1
    RDID2 = const(0xDB)  # Read ID 2
    RDID3 = const(0xDC)  # Read ID 3
    RDID4 = const(0xDD)  # Read ID 4
    GMCTRP1 = const(0xE0)  # Positive gamma correction
    GMCTRN1 = const(0xE1)  # Negative gamma correction
    DTCA = const(0xE8)  # Driver timing control A
    DTCB = const(0xEA)  # Driver timing control B
    POSC = const(0xED)  # Power on sequence control
    ENABLE3G = const(0xF2)  # Enable 3 gamma control
    PUMPRC = const(0xF7)  # Pump ratio control

    ROTATE = {
        0: 0x88,
        90: 0xE8,
        180: 0x48,
        270: 0x28
    }
    
    
    #spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
    def __init__(self, dc=Pin(8), cs=Pin(9), rst=Pin(12),
                 width=320, height=240,rotation=90, backlight=13):
        """Initialize TFT.

        Args:
            spi (Class Spi):  SPI interface for display
            cs (Class Pin):  Chip select pin
            dc (Class Pin):  Data/Command pin
            rst (Class Pin):  Reset pin
            width (Optional int): Screen width (default 320)
            height (Optional int): Screen height (default 240)
            rotation (Optional int): Rotation must be 90 default, 0 or 180 or 270
        """
        self.spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.width = width
        self.height = height
        self.backlight = Pin(backlight, Pin.OUT)
        self.backlight.value(1)
        
        if rotation not in self.ROTATE.keys():
            raise RuntimeError('Rotation must be 0, 90, 180 or 270.')
        else:
            self.rotation = self.ROTATE[rotation]

        # Initialize GPIO pins and set implementation specific methods
        if implementation.name == 'circuitpython':
            self.cs.switch_to_output(value=True)
            self.dc.switch_to_output(value=False)
            self.rst.switch_to_output(value=True)
            self.reset = self.reset_cpy
            self.write_cmd = self.write_cmd_cpy
            self.write_data = self.write_data_cpy
        else:
            self.cs.init(self.cs.OUT, value=1)
            self.dc.init(self.dc.OUT, value=0)
            self.rst.init(self.rst.OUT, value=1)
            self.reset = self.reset_mpy
            self.write_cmd = self.write_cmd_mpy
            self.write_data = self.write_data_mpy
        self.reset()
        # Send initialization commands
        self.write_cmd(self.SWRESET)  # Software reset
        sleep(.1)
        self.write_cmd(self.PWCTRB, 0x00, 0xC1, 0x30)  # Pwr ctrl B
        self.write_cmd(self.POSC, 0x64, 0x03, 0x12, 0x81)  # Pwr on seq. ctrl
        self.write_cmd(self.DTCA, 0x85, 0x00, 0x78)  # Driver timing ctrl A
        self.write_cmd(self.PWCTRA, 0x39, 0x2C, 0x00, 0x34, 0x02)  # Pwr ctrl A
        self.write_cmd(self.PUMPRC, 0x20)  # Pump ratio control
        self.write_cmd(self.DTCB, 0x00, 0x00)  # Driver timing ctrl B
        self.write_cmd(self.PWCTR1, 0x23)  # Pwr ctrl 1
        self.write_cmd(self.PWCTR2, 0x10)  # Pwr ctrl 2
        self.write_cmd(self.VMCTR1, 0x3E, 0x28)  # VCOM ctrl 1
        self.write_cmd(self.VMCTR2, 0x86)  # VCOM ctrl 2
        self.write_cmd(self.MADCTL, self.rotation)  # Memory access ctrl
        self.write_cmd(self.VSCRSADD, 0x00)  # Vertical scrolling start address
        self.write_cmd(self.PIXFMT, 0x55)  # COLMOD: Pixel format
        self.write_cmd(self.FRMCTR1, 0x00, 0x18)  # Frame rate ctrl
        self.write_cmd(self.DFUNCTR, 0x08, 0x82, 0x27)
        self.write_cmd(self.ENABLE3G, 0x00)  # Enable 3 gamma ctrl
        self.write_cmd(self.GAMMASET, 0x01)  # Gamma curve selected
        self.write_cmd(self.GMCTRP1, 0x0F, 0x31, 0x2B, 0x0C, 0x0E, 0x08, 0x4E,
                       0xF1, 0x37, 0x07, 0x10, 0x03, 0x0E, 0x09, 0x00)
        self.write_cmd(self.GMCTRN1, 0x00, 0x0E, 0x14, 0x03, 0x11, 0x07, 0x31,
                       0xC1, 0x48, 0x08, 0x0F, 0x0C, 0x31, 0x36, 0x0F)
        self.write_cmd(self.SLPOUT)  # Exit sleep
        sleep(.1)
        self.write_cmd(self.DISPLAY_ON)  # Display on
        sleep(.1)
        self.clear()
    
    def backlight_off(self):
        self.backlight.value(0)
        
    def backlight_on(self):
        self.backlight.value(1)
        
    def block(self, x0, y0, x1, y1, data):
        """Write a block of data to display.

        Args:
            x0 (int):  Starting X position.
            y0 (int):  Starting Y position.
            x1 (int):  Ending X position.
            y1 (int):  Ending Y position.
            data (bytes): Data buffer to write.
        """
        self.write_cmd(self.SET_COLUMN, *ustruct.pack(">HH", x0, x1))
        self.write_cmd(self.SET_PAGE, *ustruct.pack(">HH", y0, y1))

        self.write_cmd(self.WRITE_RAM)
        self.write_data(data)

    def cleanup(self):
        """Clean up resources."""
        self.clear()
        self.display_off()
        self.spi.deinit()
        print('display off')

    def clear(self, color=0):
        """Clear display.

        Args:
            color (Optional int): RGB565 color value (Default: 0 = Black).
        """
        w = self.width
        h = self.height
        # Clear display in 1024 byte blocks
        if color:
            line = color.to_bytes(2, 'big') * (w * 8)
        else:
            line = bytearray(w * 16)
        for y in range(0, h, 8):
            self.block(0, y, w - 1, y + 7, line)

    def display_off(self):
        """Turn display off."""
        self.write_cmd(self.DISPLAY_OFF)

    def display_on(self):
        """Turn display on."""
        self.write_cmd(self.DISPLAY_ON)

    def draw_circle(self, x0, y0, r, color):
        """Draw a circle.

        Args:
            x0 (int): X coordinate of center point.
            y0 (int): Y coordinate of center point.
            r (int): Radius.
            color (int): RGB565 color value.
        """
        f = 1 - r
        dx = 1
        dy = -r - r
        x = 0
        y = r
        self.draw_pixel(x0, y0 + r, color)
        self.draw_pixel(x0, y0 - r, color)
        self.draw_pixel(x0 + r, y0, color)
        self.draw_pixel(x0 - r, y0, color)
        while x < y:
            if f >= 0:
                y -= 1
                dy += 2
                f += dy
            x += 1
            dx += 2
            f += dx
            self.draw_pixel(x0 + x, y0 + y, color)
            self.draw_pixel(x0 - x, y0 + y, color)
            self.draw_pixel(x0 + x, y0 - y, color)
            self.draw_pixel(x0 - x, y0 - y, color)
            self.draw_pixel(x0 + y, y0 + x, color)
            self.draw_pixel(x0 - y, y0 + x, color)
            self.draw_pixel(x0 + y, y0 - x, color)
            self.draw_pixel(x0 - y, y0 - x, color)

    def draw_ellipse(self, x0, y0, a, b, color):
        """Draw an ellipse.

        Args:
            x0, y0 (int): Coordinates of center point.
            a (int): Semi axis horizontal.
            b (int): Semi axis vertical.
            color (int): RGB565 color value.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the axes are integer rounded
            up to complete on a full pixel.  Therefore the major and
            minor axes are increased by 1.
        """
        a2 = a * a
        b2 = b * b
        twoa2 = a2 + a2
        twob2 = b2 + b2
        x = 0
        y = b
        px = 0
        py = twoa2 * y
        # Plot initial points
        self.draw_pixel(x0 + x, y0 + y, color)
        self.draw_pixel(x0 - x, y0 + y, color)
        self.draw_pixel(x0 + x, y0 - y, color)
        self.draw_pixel(x0 - x, y0 - y, color)
        # Region 1
        p = round(b2 - (a2 * b) + (0.25 * a2))
        while px < py:
            x += 1
            px += twob2
            if p < 0:
                p += b2 + px
            else:
                y -= 1
                py -= twoa2
                p += b2 + px - py
            self.draw_pixel(x0 + x, y0 + y, color)
            self.draw_pixel(x0 - x, y0 + y, color)
            self.draw_pixel(x0 + x, y0 - y, color)
            self.draw_pixel(x0 - x, y0 - y, color)
        # Region 2
        p = round(b2 * (x + 0.5) * (x + 0.5) +
                  a2 * (y - 1) * (y - 1) - a2 * b2)
        while y > 0:
            y -= 1
            py -= twoa2
            if p > 0:
                p += a2 - py
            else:
                x += 1
                px += twob2
                p += a2 - py + px
            self.draw_pixel(x0 + x, y0 + y, color)
            self.draw_pixel(x0 - x, y0 + y, color)
            self.draw_pixel(x0 + x, y0 - y, color)
            self.draw_pixel(x0 - x, y0 - y, color)

    def draw_hline(self, x, y, w, color):
        """Draw a horizontal line.

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            w (int): Width of line.
            color (int): RGB565 color value.
        """
        if self.is_off_grid(x, y, x + w - 1, y):
            return
        line = color.to_bytes(2, 'big') * w
        self.block(x, y, x + w - 1, y, line)

    def draw_image(self, path, x=0, y=0, w=320, h=240):
        """Draw image from flash.

        Args:
            path (string): Image file path.
            x (int): X coordinate of image left.  Default is 0.
            y (int): Y coordinate of image top.  Default is 0.
            w (int): Width of image.  Default is 320.
            h (int): Height of image.  Default is 240.
        """
        x2 = x + w - 1
        y2 = y + h - 1
        if self.is_off_grid(x, y, x2, y2):
            return
        with open(path, "rb") as f:
            chunk_height = 1024 // w
            chunk_count, remainder = divmod(h, chunk_height)
            chunk_size = chunk_height * w * 2
            chunk_y = y
            if chunk_count:
                for c in range(0, chunk_count):
                    buf = f.read(chunk_size)
                    self.block(x, chunk_y,
                               x2, chunk_y + chunk_height - 1,
                               buf)
                    chunk_y += chunk_height
            if remainder:
                buf = f.read(remainder * w * 2)
                self.block(x, chunk_y,
                           x2, chunk_y + remainder - 1,
                           buf)

    def draw_letter(self, x, y, letter, font, color, background=0,
                    landscape=False):
        """Draw a letter.

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            letter (string): Letter to draw.
            font (XglcdFont object): Font.
            color (int): RGB565 color value.
            background (int): RGB565 background color (default: black).
            landscape (bool): Orientation (default: False = portrait)
        """
        buf, w, h = font.get_letter(letter, color, background, landscape)
        # Check for errors (Font could be missing specified letter)
        if w == 0:
            return w, h

        if landscape:
            y -= w
            if self.is_off_grid(x, y, x + h - 1, y + w - 1):
                return 0, 0
            self.block(x, y,
                       x + h - 1, y + w - 1,
                       buf)
        else:
            if self.is_off_grid(x, y, x + w - 1, y + h - 1):
                return 0, 0
            self.block(x, y,
                       x + w - 1, y + h - 1,
                       buf)
        return w, h

    def draw_line(self, x1, y1, x2, y2, color):
        """Draw a line using Bresenham's algorithm.

        Args:
            x1, y1 (int): Starting coordinates of the line
            x2, y2 (int): Ending coordinates of the line
            color (int): RGB565 color value.
        """
        # Check for horizontal line
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            self.draw_hline(x1, y1, x2 - x1 + 1, color)
            return
        # Check for vertical line
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            self.draw_vline(x1, y1, y2 - y1 + 1, color)
            return
        # Confirm coordinates in boundary
        if self.is_off_grid(min(x1, x2), min(y1, y2),
                            max(x1, x2), max(y1, y2)):
            return
        # Changes in x, y
        dx = x2 - x1
        dy = y2 - y1
        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)
        # Rotate line
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        # Swap start and end points if necessary
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1
        # Calculate error
        error = dx >> 1
        ystep = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2 + 1):
            # Had to reverse HW ????
            if not is_steep:
                self.draw_pixel(x, y, color)
            else:
                self.draw_pixel(y, x, color)
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx

    def draw_lines(self, coords, color):
        """Draw multiple lines.

        Args:
            coords ([[int, int],...]): Line coordinate X, Y pairs
            color (int): RGB565 color value.
        """
        # Starting point
        x1, y1 = coords[0]
        # Iterate through coordinates
        for i in range(1, len(coords)):
            x2, y2 = coords[i]
            self.draw_line(x1, y1, x2, y2, color)
            x1, y1 = x2, y2

    def draw_pixel(self, x, y, color):
        """Draw a single pixel.

        Args:
            x (int): X position.
            y (int): Y position.
            color (int): RGB565 color value.
        """
        if self.is_off_grid(x, y, x, y):
            return
        self.block(x, y, x, y, color.to_bytes(2, 'big'))

    def draw_polygon(self, sides, x0, y0, r, color, rotate=0):
        """Draw an n-sided regular polygon.

        Args:
            sides (int): Number of polygon sides.
            x0, y0 (int): Coordinates of center point.
            r (int): Radius.
            color (int): RGB565 color value.
            rotate (Optional float): Rotation in degrees relative to origin.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the radius is integer rounded
            up to complete on a full pixel.  Therefore diameter = 2 x r + 1.
        """
        coords = []
        theta = radians(rotate)
        n = sides + 1
        for s in range(n):
            t = 2.0 * pi * s / sides + theta
            coords.append([int(r * cos(t) + x0), int(r * sin(t) + y0)])

        # Cast to python float first to fix rounding errors
        self.draw_lines(coords, color=color)

    def draw_rectangle(self, x, y, w, h, color):
        """Draw a rectangle.

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            w (int): Width of rectangle.
            h (int): Height of rectangle.
            color (int): RGB565 color value.
        """
        x2 = x + w - 1
        y2 = y + h - 1
        self.draw_hline(x, y, w, color)
        self.draw_hline(x, y2, w, color)
        self.draw_vline(x, y, h, color)
        self.draw_vline(x2, y, h, color)

    def draw_sprite(self, buf, x, y, w, h):
        """Draw a sprite (optimized for horizontal drawing).

        Args:
            buf (bytearray): Buffer to draw.
            x (int): Starting X position.
            y (int): Starting Y position.
            w (int): Width of drawing.
            h (int): Height of drawing.
        """
        x2 = x + w - 1
        y2 = y + h - 1
        if self.is_off_grid(x, y, x2, y2):
            return
        self.block(x, y, x2, y2, buf)

    def draw_text(self, x, y, text, font, color,  background=0,
                  landscape=False, spacing=1):
        """Draw text.

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            text (string): Text to draw.
            font (XglcdFont object): Font.
            color (int): RGB565 color value.
            background (int): RGB565 background color (default: black).
            landscape (bool): Orientation (default: False = portrait)
            spacing (int): Pixels between letters (default: 1)
        """
        for letter in text:
            # Get letter array and letter dimensions
            w, h = self.draw_letter(x, y, letter, font, color, background,
                                    landscape)
            # Stop on error
            if w == 0 or h == 0:
                print('Invalid width {0} or height {1}'.format(w, h))
                return

            if landscape:
                # Fill in spacing
                if spacing:
                    self.fill_hrect(x, y - w - spacing, h, spacing, background)
                # Position y for next letter
                y -= (w + spacing)
            else:
                # Fill in spacing
                if spacing:
                    self.fill_hrect(x + w, y, spacing, h, background)
                # Position x for next letter
                x += (w + spacing)

                # # Fill in spacing
                # if spacing:
                #     self.fill_vrect(x + w, y, spacing, h, background)
                # # Position x for next letter
                # x += w + spacing

    def draw_text8x8(self, x, y, text, color,  background=0,
                     rotate=0):
        """Draw text using built-in MicroPython 8x8 bit font.

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            text (string): Text to draw.
            color (int): RGB565 color value.
            background (int): RGB565 background color (default: black).
            rotate(int): 0, 90, 180, 270
        """
        w = len(text) * 8
        h = 8
        # Confirm coordinates in boundary
        if self.is_off_grid(x, y, x + 7, y + 7):
            return
        # Rearrange color
        r = (color & 0xF800) >> 8
        g = (color & 0x07E0) >> 3
        b = (color & 0x1F) << 3
        buf = bytearray(w * 16)
        fbuf = FrameBuffer(buf, w, h, RGB565)
        if background != 0:
            bg_r = (background & 0xF800) >> 8
            bg_g = (background & 0x07E0) >> 3
            bg_b = (background & 0x1F) << 3
            fbuf.fill(RGB(bg_b, bg_r, bg_g))
        fbuf.text(text, 0, 0, RGB(b, r, g))
        if rotate == 0:
            self.block(x, y, x + w - 1, y + (h - 1), buf)
        elif rotate == 90:
            buf2 = bytearray(w * 16)
            fbuf2 = FrameBuffer(buf2, h, w, RGB565)
            for y1 in range(h):
                for x1 in range(w):
                    fbuf2.pixel(y1, x1,
                                fbuf.pixel(x1, (h - 1) - y1))
            self.block(x, y, x + (h - 1), y + w - 1, buf2)
        elif rotate == 180:
            buf2 = bytearray(w * 16)
            fbuf2 = FrameBuffer(buf2, w, h, RGB565)
            for y1 in range(h):
                for x1 in range(w):
                    fbuf2.pixel(x1, y1,
                                fbuf.pixel((w - 1) - x1, (h - 1) - y1))
            self.block(x, y, x + w - 1, y + (h - 1), buf2)
        elif rotate == 270:
            buf2 = bytearray(w * 16)
            fbuf2 = FrameBuffer(buf2, h, w, RGB565)
            for y1 in range(h):
                for x1 in range(w):
                    fbuf2.pixel(y1, x1,
                                fbuf.pixel((w - 1) - x1, y1))
            self.block(x, y, x + (h - 1), y + w - 1, buf2)

    def draw_vline(self, x, y, h, color):
        """Draw a vertical line.

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            h (int): Height of line.
            color (int): RGB565 color value.
        """
        # Confirm coordinates in boundary
        if self.is_off_grid(x, y, x, y + h - 1):
            return
        line = color.to_bytes(2, 'big') * h
        self.block(x, y, x, y + h - 1, line)

    def fill_circle(self, x0, y0, r, color):
        """Draw a filled circle.

        Args:
            x0 (int): X coordinate of center point.
            y0 (int): Y coordinate of center point.
            r (int): Radius.
            color (int): RGB565 color value.
        """
        f = 1 - r
        dx = 1
        dy = -r - r
        x = 0
        y = r
        self.draw_vline(x0, y0 - r, 2 * r + 1, color)
        while x < y:
            if f >= 0:
                y -= 1
                dy += 2
                f += dy
            x += 1
            dx += 2
            f += dx
            self.draw_vline(x0 + x, y0 - y, 2 * y + 1, color)
            self.draw_vline(x0 - x, y0 - y, 2 * y + 1, color)
            self.draw_vline(x0 - y, y0 - x, 2 * x + 1, color)
            self.draw_vline(x0 + y, y0 - x, 2 * x + 1, color)

    def fill_ellipse(self, x0, y0, a, b, color):
        """Draw a filled ellipse.

        Args:
            x0, y0 (int): Coordinates of center point.
            a (int): Semi axis horizontal.
            b (int): Semi axis vertical.
            color (int): RGB565 color value.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the axes are integer rounded
            up to complete on a full pixel.  Therefore the major and
            minor axes are increased by 1.
        """
        a2 = a * a
        b2 = b * b
        twoa2 = a2 + a2
        twob2 = b2 + b2
        x = 0
        y = b
        px = 0
        py = twoa2 * y
        # Plot initial points
        self.draw_line(x0, y0 - y, x0, y0 + y, color)
        # Region 1
        p = round(b2 - (a2 * b) + (0.25 * a2))
        while px < py:
            x += 1
            px += twob2
            if p < 0:
                p += b2 + px
            else:
                y -= 1
                py -= twoa2
                p += b2 + px - py
            self.draw_line(x0 + x, y0 - y, x0 + x, y0 + y, color)
            self.draw_line(x0 - x, y0 - y, x0 - x, y0 + y, color)
        # Region 2
        p = round(b2 * (x + 0.5) * (x + 0.5) +
                  a2 * (y - 1) * (y - 1) - a2 * b2)
        while y > 0:
            y -= 1
            py -= twoa2
            if p > 0:
                p += a2 - py
            else:
                x += 1
                px += twob2
                p += a2 - py + px
            self.draw_line(x0 + x, y0 - y, x0 + x, y0 + y, color)
            self.draw_line(x0 - x, y0 - y, x0 - x, y0 + y, color)

    def fill_hrect(self, x, y, w, h, color):
        """Draw a filled rectangle (optimized for horizontal drawing).

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            w (int): Width of rectangle.
            h (int): Height of rectangle.
            color (int): RGB565 color value.
        """
        if self.is_off_grid(x, y, x + w - 1, y + h - 1):
            return
        chunk_height = 1024 // w
        chunk_count, remainder = divmod(h, chunk_height)
        chunk_size = chunk_height * w
        chunk_y = y
        if chunk_count:
            buf = color.to_bytes(2, 'big') * chunk_size
            for c in range(0, chunk_count):
                self.block(x, chunk_y,
                           x + w - 1, chunk_y + chunk_height - 1,
                           buf)
                chunk_y += chunk_height

        if remainder:
            buf = color.to_bytes(2, 'big') * remainder * w
            self.block(x, chunk_y,
                       x + w - 1, chunk_y + remainder - 1,
                       buf)

    def fill_rectangle(self, x, y, w, h, color):
        """Draw a filled rectangle.

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            w (int): Width of rectangle.
            h (int): Height of rectangle.
            color (int): RGB565 color value.
        """
        if self.is_off_grid(x, y, x + w - 1, y + h - 1):
            return
        if w > h:
            self.fill_hrect(x, y, w, h, color)
        else:
            self.fill_vrect(x, y, w, h, color)

    def fill_polygon(self, sides, x0, y0, r, color, rotate=0):
        """Draw a filled n-sided regular polygon.

        Args:
            sides (int): Number of polygon sides.
            x0, y0 (int): Coordinates of center point.
            r (int): Radius.
            color (int): RGB565 color value.
            rotate (Optional float): Rotation in degrees relative to origin.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the radius is integer rounded
            up to complete on a full pixel.  Therefore diameter = 2 x r + 1.
        """
        # Determine side coordinates
        coords = []
        theta = radians(rotate)
        n = sides + 1
        for s in range(n):
            t = 2.0 * pi * s / sides + theta
            coords.append([int(r * cos(t) + x0), int(r * sin(t) + y0)])
        # Starting point
        x1, y1 = coords[0]
        # Minimum Maximum X dict
        xdict = {y1: [x1, x1]}
        # Iterate through coordinates
        for row in coords[1:]:
            x2, y2 = row
            xprev, yprev = x2, y2
            # Calculate perimeter
            # Check for horizontal side
            if y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 in xdict:
                    xdict[y1] = [min(x1, xdict[y1][0]), max(x2, xdict[y1][1])]
                else:
                    xdict[y1] = [x1, x2]
                x1, y1 = xprev, yprev
                continue
            # Non horizontal side
            # Changes in x, y
            dx = x2 - x1
            dy = y2 - y1
            # Determine how steep the line is
            is_steep = abs(dy) > abs(dx)
            # Rotate line
            if is_steep:
                x1, y1 = y1, x1
                x2, y2 = y2, x2
            # Swap start and end points if necessary
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            # Recalculate differentials
            dx = x2 - x1
            dy = y2 - y1
            # Calculate error
            error = dx >> 1
            ystep = 1 if y1 < y2 else -1
            y = y1
            # Calcualte minimum and maximum x values
            for x in range(x1, x2 + 1):
                if is_steep:
                    if x in xdict:
                        xdict[x] = [min(y, xdict[x][0]), max(y, xdict[x][1])]
                    else:
                        xdict[x] = [y, y]
                else:
                    if y in xdict:
                        xdict[y] = [min(x, xdict[y][0]), max(x, xdict[y][1])]
                    else:
                        xdict[y] = [x, x]
                error -= abs(dy)
                if error < 0:
                    y += ystep
                    error += dx
            x1, y1 = xprev, yprev
        # Fill polygon
        for y, x in xdict.items():
            self.draw_hline(x[0], y, x[1] - x[0] + 2, color)

    def fill_vrect(self, x, y, w, h, color):
        """Draw a filled rectangle (optimized for vertical drawing).

        Args:
            x (int): Starting X position.
            y (int): Starting Y position.
            w (int): Width of rectangle.
            h (int): Height of rectangle.
            color (int): RGB565 color value.
        """
        if self.is_off_grid(x, y, x + w - 1, y + h - 1):
            return
        chunk_width = 1024 // h
        chunk_count, remainder = divmod(w, chunk_width)
        chunk_size = chunk_width * h
        chunk_x = x
        if chunk_count:
            buf = color.to_bytes(2, 'big') * chunk_size
            for c in range(0, chunk_count):
                self.block(chunk_x, y,
                           chunk_x + chunk_width - 1, y + h - 1,
                           buf)
                chunk_x += chunk_width

        if remainder:
            buf = color.to_bytes(2, 'big') * remainder * h
            self.block(chunk_x, y,
                       chunk_x + remainder - 1, y + h - 1,
                       buf)

    def is_off_grid(self, xmin, ymin, xmax, ymax):
        """Check if coordinates extend past display boundaries.

        Args:
            xmin (int): Minimum horizontal pixel.
            ymin (int): Minimum vertical pixel.
            xmax (int): Maximum horizontal pixel.
            ymax (int): Maximum vertical pixel.
        Returns:
            boolean: False = Coordinates OK, True = Error.
        """
        if xmin < 0:
            print('x-coordinate: {0} below minimum of 0.'.format(xmin))
            return True
        if ymin < 0:
            print('y-coordinate: {0} below minimum of 0.'.format(ymin))
            return True
        if xmax >= self.width:
            print('x-coordinate: {0} above maximum of {1}.'.format(
                xmax, self.width - 1))
            return True
        if ymax >= self.height:
            print('y-coordinate: {0} above maximum of {1}.'.format(
                ymax, self.height - 1))
            return True
        return False

    def load_sprite(self, path, w, h):
        """Load sprite image.

        Args:
            path (string): Image file path.
            w (int): Width of image.
            h (int): Height of image.
        Notes:
            w x h cannot exceed 2048
        """
        buf_size = w * h * 2
        with open(path, "rb") as f:
            return f.read(buf_size)

    def reset_cpy(self):
        """Perform reset: Low=initialization, High=normal operation.

        Notes: CircuitPython implemntation
        """
        self.rst.value = False
        sleep(.05)
        self.rst.value = True
        sleep(.05)

    def reset_mpy(self):
        """Perform reset: Low=initialization, High=normal operation.

        Notes: MicroPython implemntation
        """
        self.rst(0)
        sleep(.05)
        self.rst(1)
        sleep(.05)

    def scroll(self, y):
        """Scroll display vertically.

        Args:
            y (int): Number of pixels to scroll display.
        """
        self.write_cmd(self.VSCRSADD, y >> 8, y & 0xFF)

    def set_scroll(self, top, bottom):
        """Set the height of the top and bottom scroll margins.

        Args:
            top (int): Height of top scroll margin
            bottom (int): Height of bottom scroll margin
        """
        if top + bottom <= self.height:
            middle = self.height - (top + bottom)
            print(top, middle, bottom)
            self.write_cmd(self.VSCRDEF,
                           top >> 8,
                           top & 0xFF,
                           middle >> 8,
                           middle & 0xFF,
                           bottom >> 8,
                           bottom & 0xFF)

    def sleep(self, enable=True):
        """Enters or exits sleep mode.

        Args:
            enable (bool): True (default)=Enter sleep mode, False=Exit sleep
        """
        if enable:
            self.write_cmd(self.SLPIN)
        else:
            self.write_cmd(self.SLPOUT)


    def write_cmd_mpy(self, command, *args):
        """Write command to TFT (MicroPython).

        Args:
            command (byte): ILI9341 command code.
            *args (optional bytes): Data to transmit.
        """
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([command]))
        self.cs(1)
        # Handle any passed data
        if len(args) > 0:
            self.write_data(bytearray(args))

    def write_cmd_cpy(self, command, *args):
        """Write command to TFT (CircuitPython).

        Args:
            command (byte): ILI9341 command code.
            *args (optional bytes): Data to transmit.
        """
        self.dc.value = False
        self.cs.value = False
        # Confirm SPI locked before writing
        while not self.spi.try_lock():
            pass
        self.spi.write(bytearray([command]))
        self.spi.unlock()
        self.cs.value = True
        # Handle any passed data
        if len(args) > 0:
            self.write_data(bytearray(args))

    def write_data_mpy(self, data):
        """Write data to TFT (MicroPython).

        Args:
            data (bytes): Data to transmit.
        """
        self.dc(1)
        self.cs(0)
        self.spi.write(data)
        self.cs(1)

    def write_data_cpy(self, data):
        """Write data to TFT (CircuitPython).

        Args:
            data (bytes): Data to transmit.
        """
        self.dc.value = True
        self.cs.value = False
        # Confirm SPI locked before writing
        while not self.spi.try_lock():
            pass
        self.spi.write(data)
        self.spi.unlock()
        self.cs.value = True


class TOUCH:
    """
    A driver for the FocalTech capacitive touch sensor.
    """

    _debug = False
    chip = None
    
    def __init__(self, i2c=I2C(1,sda=Pin(2), scl=Pin(3)), address=_FT6206_DEFAULT_I2C_ADDR, debug=False):
        self.bus = i2c
        self.address = address 
        self._debug = debug
        
        print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
        print("I2C Configuration: "+str(i2c))                   # Display I2C config
        print('Scan i2c bus...')
        devices = i2c.scan()
        print(devices)

        if len(devices) == 0:
              print("No i2c device !")
        else:
             print('i2c devices found:',len(devices))

        for device in devices:
             print("Decimal address: ",device," | Hexa address: ",hex(device))

        chip_data = self._read(_FT6XXX_REG_LIBH, 8)
        lib_ver, chip_id, _, _, firm_id, _, vend_id = struct.unpack(
            ">HBBBBBB", chip_data
        )

        if debug:
            print("Vendor ID %02x" % vend_id)

        self.vend_id=vend_id
        if chip_id == 0x06:
            self.chip = "FT6206"
        elif chip_id == 0x64:
            self.chip = "FT6236"

        elif debug:
            print("Chip Id: %02x" % chip_id)

        if debug:
            print("Library vers %04X" % lib_ver)
            print("Firmware ID %02X" % firm_id)
            print("Point rate %d Hz" % self._read(_FT6XXX_REG_POINTRATE, 1)[0])
            print("Thresh %d" % self._read(_FT6XXX_REG_THRESHHOLD, 1)[0])
            

    @property
    def touched(self):
        """ Returns the number of touches currently detected """
        return self._read(_FT6XXX_REG_NUMTOUCHES, 1)[0]

    # pylint: disable=unused-variable
    @property
    def touches(self):
        """
        Returns a list of touchpoint dicts, with 'x' and 'y' containing the
        touch coordinates, and 'id' as the touch # for multitouch tracking
        """
        touchpoints = []
        data = self._read(_FT6XXX_REG_DATA, 32)

        for i in range(2):
            point_data = data[i * 6 + 3 : i * 6 + 9]
            if all([i == 0xFF for i in point_data]):
                continue
            # print([hex(i) for i in point_data])
            x, y, weight, misc = struct.unpack(">HHBB", point_data)
            # print(x, y, weight, misc)
            touch_id = y >> 12
            x &= 0xFFF
            y &= 0xFFF
            #interchange x, y Co-ordinates to match x, y of display  
            y1 = self.touch_Map(x,0,240,0,240)
            x1 = self.touch_Map(y,0,320,320,0)
            point = {"x": x1, "y": y1, "id": touch_id}
            touchpoints.append(point)
        return touchpoints

    def _read(self, reg, length):
        """Returns an array of 'length' bytes from the 'register'"""
        result = bytearray(length)
        self.bus.readfrom_mem_into(self.address, reg, result)
        if self._debug:
            print("\t$%02X => %s" % (reg, [hex(i) for i in result]))
        return result

    def _write(self, reg, values):
        """Writes an array of 'length' bytes to the 'register'"""
        values = [(v & 0xFF) for v in values]
        self.bus.writeto_mem(self.address,reg,bytes(values))
        if self._debug:
            print("\t$%02X <= %s" % (reg, [hex(i) for i in values]))

    def touch_Map(self, x, in_min, in_max, out_min, out_max):
        """ Mapping 0 - 180 range into 0 - 1024
        """
        return round((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    def getXY(self):
        lst = self.touches
        #print(lst)
        if len(lst)>0:
            lst = lst[0]
            x = lst['x']
            y = lst['y']
            return x,y



