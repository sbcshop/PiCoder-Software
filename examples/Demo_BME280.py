''' Demo how to read temperature, Pressure and humidity using onboard BME280 sensor of PiCoder '''
from picoder import BME280 #include BME280 module from picoder library
from time import sleep

#create instance of class
sense = BME280()

while 1:
    t = sense.temperature() # provides temperature in Degrees
    p = sense.pressure() 	# provides pressure in hPa
    h = sense.humidity()	# provides relative Humidity in percentage
    print(f"Temperature = {t}, Pressure = {p}, Humidity = {h}")
    sleep(0.2) 


