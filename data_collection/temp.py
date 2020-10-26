#!/usr/bin/python
"""I2C temperature/humidity sensor functions
Sets up I2C connection for AHT20 sensor
Reads in data over I2C
Source: https://circuitpython.readthedocs.io/projects/ahtx0/en/latest/
"""
from time import sleep
import board
import busio
import adafruit_ahtx0

def setup_temp():
    # Create library object using our Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_ahtx0.AHTx0(i2c)
    return

def data_temp(delay):
    while True:
        print("\nTemperature: %0.1f C" % sensor.temperature)
        print("Humidity: %0.1f %%" % sensor.relative_humidity)
        sleep(delay)
    return sensor.temperature, sensor.relative_humidity
