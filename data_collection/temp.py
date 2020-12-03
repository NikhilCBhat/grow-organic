#!/usr/bin/env python3
"""I2C temperature/humidity sensor setup, read, upload data

Sets up I2C connection for AHT20 sensor
Reads in data over I2C
Source: https://circuitpython.readthedocs.io/projects/ahtx0/en/latest/
"""
import sys
sys.path.append('.')

from time import sleep
import board
import busio
import adafruit_ahtx0
from sensor_data.upload_sensor_data import upload_data

def temp_setup():
    # Create library object using our Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_ahtx0.AHTx0(i2c)
    return sensor

def collect_data(sensor):
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
    return temperature, humidity

def print_data(sensor):
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    return

def upload_data_to_sensor_table(temp_data):
    sensor_names = ["TEMPERATURE", "HUMIDITY"]
    for sensor_name, data in zip(sensor_names, temp_data):
        upload_data(0, sensor_name, data)

def main(temp_sensor):
    print_data(temp_sensor)
#    temp_data = collect_data(temp_sensor)
#    upload_data_to_sensor_table(temp_data)
#    sleep(10)

if __name__ == "__main__":
    main()
