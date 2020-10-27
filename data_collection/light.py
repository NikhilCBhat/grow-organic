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

def setup_light():
    sensor = SI1145.SI1145()

    print('Press Cntrl + Z to cancel')
    return
def data_light(delay):
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