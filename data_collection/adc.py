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
    return chan0, chan1, chan2, chan3

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)


def adc_data(delay, chan0, chan1, chan2, chan3):
    print("{:>5}\t{:>5}".format('raw', 'v'))

    while True:
        print("Temp {:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage))
        print("Wind {:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
    #    print("Soil1 {:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
    #    print("Soil2 {:>5}\t{:>5.3f}".format(chan3.value, chan3.voltage))

        sleep(delay)
    return chan0.value, chan1.value, chan2.value, chan3.value

# TODO: Write function to determine data type
# needs to read in data, determine if wind or moisture
# needs to output useable data for calibration
def data_type(chan0, chan1, chan2, chan3):
    soil1 = chan2.value
    soil2 = chan3.value

    wind = chan1.value
    wind_temp = chan0.value

    return soil1, soil2, wind, wind_temp

def wind_data(wind, wind_temp):
    if wind >= 27000:
        print("Fan is on high {}".format(wind))
    elif (wind < 27000) and (wind >= 25000):
        print("Fan is on medium {}".format(wind))
    elif (wind < 25000) and(wind >= 20000):
        print("Fan is on low {}".format(wind))
    else:
        print("Fan is not on {}".format(wind))
    return

def moisture_data(soil, sensor_number):
    if soil >= 16000:
        print("Soil {} is very dry {}".format(sensor_number, soil))
    elif (soil < 16000) and (soil >= 10000):
        print("Soil {} is in the Middle {} - Need to calibrate better".format(sensor_number, soil))
    else:
        print("Soil {} is in water {}".format(sensor_number, soil))
    return

def main():
    (chan0, chan1, chan2, chan3) = setup_adc()
    while True:
    #     (data0, data1, data2, data3) = adc_data(1, chan0, chan1, chan2, chan3)
    #    upload_data_to_sensor_table(adc_data)
        (soil1, soil2, wind, wind_temp) = data_type(chan0, chan1, chan2, chan3)
        moisture_data(soil1, 1)
        wind_data(wind, wind_temp)
        moisture_data(soil2, 2)
    #    (data0, data1, data2, data3) = data_type(chan0, chan1, chan2, chan3)
        sleep(2)

if __name__ == "__main__":
    main()
