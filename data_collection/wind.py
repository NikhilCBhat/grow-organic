#!/usr/bin/python
"""ADC setup and data collection function for wind sensor
Sets up I2C connections for all analog input channels
Reads in data from channels
ADC Source: https://circuitpython.readthedocs.io/projects/ads1x15/en/latest/
Wind Source: https://github.com/moderndevice/Wind_Sensor/
https://moderndevice.com/product/wind-sensor/
"""

from time import sleep
import math
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
#from sensor_data.upload_sensor_data import upload_data

def adc_setup():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1015(i2c)

    # Create single-ended input on all channels
    # Connect Out pin to ADC Channel 0
    # Connect RV pin to ADC Channel 1
    # Connect TMP pin to ADC Channel 2
    a_out = AnalogIn(ads, ADS.P0)
    a_rv = AnalogIn(ads, ADS.P1)
    a_temp = AnalogIn(ads, ADS.P2)
    chan3 = AnalogIn(ads, ADS.P3)
    return a_out, a_rv, a_temp

#TODO: Write calibration functions then integrate them with the rest of the system
def calibrate_wind(a_out, a_rv, a_temp):
    # ZERO_WIND needs to be determined by removing wind and adjusting
    ZERO_WIND = 0
    # the data
    value_out = a_out.value
    print("output value:", value_out)
    value_rv = a_rv.value
    print("rv value:", value_rv)
    value_temp = a_temp.value
    print("temperature value:", value_temp)

    # Calibration
    rv_wind_volts = (value_rv * 0.0048828125)
    read_wind_volts = a_rv.voltage
    print("Calculated RV Voltage: {} Read RV Voltage: {}".format(rv_wind_volts, read_wind_volts))
    #temp_cal = (0.005 *(analog_temp * analog_temp) - (16.862 * (analog_temp) + 9075.4))
#    analog_zero_wind = -0.0006 * (analog_temp * analog_temp) + 1.0727 * analog_temp + 47.172
#    zero_wind_volts = (analog_zero_wind * 0.0048828125) - ZERO_WIND
#    norm_wind_volts = ((rv_wind_volts - zero_wind_volts) /.2300)
#    print(norm_wind_volts)
#    wind_speed_mph =  math.pow(norm_wind_volts, 2.7265)
    return

# TODO: Below is not correct for the wind sensor
def collect_data(wind_speed_mph):
    return

def print_data(wind_speed_mph):
#    print("Wind speed - maybe??", wind_speed_mph)
    return

def upload_data_to_sensor_table(wind_data):
    sensor_names = ["WIND"]
    for sensor_name, data in zip(sensor_names, wind_data):
        upload_data(0, sensor_name, data)

def main():
    (analog_out, analog_rv, analog_temp) = adc_setup()
    wind_sensor = calibrate_wind(analog_out, analog_rv, analog_temp)
    print_data(wind_sensor)
#    wind_data  = collect_data(wind_sensor)
#    upload_data_to_sensor_table(wind_data)

if __name__ == "__main__":
    main()

