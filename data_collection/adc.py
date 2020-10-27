#!/usr/bin/python
"""ADC setup and data collection functions
Sets up I2C connections for all analog input channels
Reads in data from channels
Source: https://circuitpython.readthedocs.io/projects/ads1x15/en/latest/
"""

from time import sleep
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def setup_adc():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1015(i2c)

    # Create single-ended input on all channels
    chan0 = AnalogIn(ads, ADS.P0)
    chan1 = AnalogIn(ads, ADS.P1)
    chan2 = AnalogIn(ads, ADS.P2)
    chan3 = AnalogIn(ads, ADS.P3)
    return

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

def data_adc(delay):
    print("{:>5}\t{:>5}".format('raw', 'v'))

    while True:
        print("Chan0 {:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage))
        print("Chan1 {:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
        print("Chan2 {:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
        print("Chan3 {:>5}\t{:>5.3f}".format(chan3.value, chan3.voltage))

        sleep(delay)
    return chan0.value, chan1.value, chan2.value, chan3.value

# TODO: Write function to determine data type
# needs to read in data, determine if wind or moisture
# needs to output useable data for calibration 
def data_type():
    return