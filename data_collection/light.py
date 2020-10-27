#!/usr/bin/python
"""I2C light sensor functions
Sets up I2C connection for SI1145 sensor
Reads in data over I2C
Source: https://github.com/THP-JOE/Python_SI1145
"""

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

from time import sleep
import SI1145.SI1145 as SI1145
from sensor_data.upload_sensor_data import upload_data

def setup_light():
    sensor = SI1145.SI1145()

    print('Press Cntrl + Z to cancel')
    return sensor 

def collect_data(sensor):
    vis = sensor.readVisible()
    IR = sensor.readIR()
    UV = sensor.readUV()
    uvIndex = UV / 100.0  
    return vis, IR, uvIndex

def data_light(sensor, delay):
    while True:
            vis = sensor.readVisible()
            IR = sensor.readIR()
            UV = sensor.readUV()
            uvIndex = UV / 100.0
            print('Vis:             ' + str(vis))
            print('IR:              ' + str(IR))
            print('UV Index:        ' + str(uvIndex))

            sleep(delay)
    return vis, IR, uvIndex

def upload_data_to_sensor_table(light_data):
    sensor_names = ["VISIBLE", "IR", "UV"]
    for sensor_name, data in zip(sensor_names, light_data):
        upload_data(0, sensor_name, data)

def main():
    light_sensor = setup_light()
    while True:
        light_data  = collect_data(light_sensor)
        upload_data_to_sensor_table(light_data)
        sleep(10)

if __name__ == "__main__":
    main()