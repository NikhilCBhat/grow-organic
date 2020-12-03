#!/usr/bin/env python3
"""SI1145 I2C light sensor functions for setup, read, and upload data

Sets up I2C connection for SI1145 sensor
Reads in data over I2C and uploads data to database
Source: https://github.com/THP-JOE/Python_SI1145
"""

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import sys
sys.path.append('.')
from time import sleep
import SI1145.SI1145 as SI1145
from sensor_data.upload_sensor_data import upload_data

def light_setup():
    sensor = SI1145.SI1145()
    sensor.__init__()
    return sensor

def collect_data(sensor):
    vis = sensor.readVisible()
    IR = sensor.readIR()
    UV = sensor.readUV()
    uvIndex = UV / 100.0
    return vis, IR, uvIndex

def is_light_safe():
    sensor = light_setup()
    vis, ir, uv = collect_data(sensor)
    vis_thresh = 290
    uv_thresh = 50000
    return vis < vis_thresh and uv < uv_thresh

def print_data(sensor):
    vis = sensor.readVisible()
    IR = sensor.readIR()
    UV = sensor.readUV()
    uvIndex = UV / 100.0
    print('Vis:             ' + str(vis))
    print('IR:              ' + str(IR))
    print('UV Index:        ' + str(uvIndex))
    return

def upload_data_to_sensor_table(light_data):
    sensor_names = ["VISIBLE", "IR", "UV"]
    for sensor_name, data in zip(sensor_names, light_data):
        upload_data(0, sensor_name, data)

def main(light_sensor):
#    print_data(light_sensor)
    light_data  = collect_data(light_sensor)
    upload_data_to_sensor_table(light_data)

if __name__ == "__main__":
    main()
#    sensor = light_setup()
#    print("Done setup")
