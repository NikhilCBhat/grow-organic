#!/usr/bin/python
"""Soil Moisture Sensor Read
Allows for moisture sensor
Source: https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test
"""
import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

def moisture_setup(addr):
    i2c_bus = busio.I2C(SCL, SDA)
    sensor = Seesaw(i2c_bus, addr)
    return sensor

def collect_data(sensor):
    # read soil mosisture
    soil_moisture = sensor.moisture_read()
    # read temperature from the temperature sensor
    soil_temp = sensor.get_temp()
    return soil_moisture, soil_temp

def print_data(sensor):
    # read soil mosisture
    soil_moisture = sensor.moisture_read()
    # read temperature from the temperature sensor
    soil_temp = sensor.get_temp()
    print("Soil temp: " + str(soil_temp) + "  Soil moisture: " + str(soil_moisture))
    return

def upload_data_to_sensor_table(moisture_data):
    sensor_names = ["MOISTURE", "SOILTEMP"]
    for sensor_name, data in zip(sensor_names, moisture_data):
        upload_data(0, sensor_name, data)


#TODO: Figure out how to assign mulitple sensor addresses
def main()
    addr=0x36
    moisture_sensor = moisture_setup(addr)
    print_data(moisture_sensor)
#    moisture_data  = collect_data(moisture_sensor)
#    upload_data_to_sensor_table(moisture_data)

if __name__ == "__main__":
    main()
