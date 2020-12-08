#!/usr/bin/python
"""ADC setup and data collection function for wind sensor
Sets up I2C connections for all analog input channels
Reads in data from channels
ADC Source: https://circuitpython.readthedocs.io/projects/ads1x15/en/latest/
Wind Source: https://github.com/moderndevice/Wind_Sensor/
https://moderndevice.com/product/wind-sensor/
"""
import sys
sys.path.append('.')
from time import sleep
import math
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from sensor_data.upload_sensor_data import upload_data
import time
import matplotlib.pyplot as plt

def plot_and_collect_data(duration = 30):
  a_out, a_rv, a_temp = adc_setup()

  out_values, voltage_values, temp_values = [], [], []

  current_time = time.time()

  while time.time() - current_time < duration:
    print(time.time() - current_time)
    out_values.append(a_out.value)
    voltage_values.append(a_rv.value)
    temp_values.append(a_temp.value)

  plt.plot(list(range(len(out_values))), out_values, label="output")
  plt.plot(list(range(len(voltage_values))), voltage_values, label="voltage")
  plt.plot(list(range(len(temp_values))), temp_values, label="temp")

  plt.legend()
  plt.show()


def adc_setup():
  ## Create the I2C bus
  i2c = busio.I2C(board.SCL, board.SDA)
  #Create the ADC object using the I2C bus
  ads = ADS.ADS1015(i2c)

  # Create single-ended input on all channels
  # Connect Out pin to ADC Channel 0
  # Connect RV pin to ADC Channel 1
  # Connect TMP pin to ADC Channel 2
  a_out = AnalogIn(ads, ADS.P3)
  a_rv = AnalogIn(ads, ADS.P2)
  a_temp = AnalogIn(ads, ADS.P1)
  return a_rv

#TODO: Write calibration functions then integrate them with the rest of the system
def calibrate_wind(a_out, a_rv, a_temp):
  # ZERO_WIND needs to be determined by removing wind and adjusting
  ZERO_WIND = 20000
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
  analog_temp = value_temp
  temp_cal = (0.005 *(analog_temp * analog_temp) - (16.862 * (analog_temp) + 9075.4))
  analog_zero_wind = -0.0006 * (analog_temp * analog_temp) + 1.0727 * analog_temp + 47.172
  zero_wind_volts = (analog_zero_wind * 0.0048828125) - ZERO_WIND
  norm_wind_volts = ((rv_wind_volts - zero_wind_volts) /.2300)
  print(norm_wind_volts)
  wind_speed_mph = pow(norm_wind_volts, 2.7265)
  return wind_speed_mph

# TODO: Below is not correct for the wind sensor
def collect_wind_data(a_rv):
  return a_rv.value

def print_data(wind_speed_mph):
  print('Wind speed:             ' + str(wind_speed_mph))
  return

def upload_data_to_sensor_table(wind_data):
  upload_data(0, "WIND", wind_data)

def collect_and_upload_wind_data(wind_sensor):
  wind_value = collect_wind_data(wind_sensor)
  upload_data_to_sensor_table(wind_value)

def is_wind_safe():
  wind_sensor = adc_setup()
  return collect_wind_data(wind_sensor) < 20000

def main(analog_out, analog_rv, analog_temp):
#  analog_out, analog_rv, analog_temp = adc_setup()
  wind_speed_mph = calibrate_wind(analog_out, analog_rv, analog_temp)
#  print_data(wind_speed_mph)
#  wind_data = collect_data(wind_speed_mph)
  upload_data_to_sensor_table(wind_speed_mph)

if __name__ == "__main__":
  plot_and_collect_data()

