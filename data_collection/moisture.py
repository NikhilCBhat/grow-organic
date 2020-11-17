#!/usr/bin/python
"""Soil Moisture Sensor Read
Allows for moisture sensor
Source: https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test
"""
import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw
from sensor_data.upload_sensor_data import upload_data

def moisture_setup(addrresses):
    sensors = []
    for addr in addrresses:
        i2c_bus = busio.I2C(SCL, SDA)
        sensor = Seesaw(i2c_bus, addr)
        sensors.append(sensor)
    return sensors

def collect_data(sensors):
    # read soil mosisture
    moisutures, temps = [], []
    for sensor in sensors:
        soil_moisture = sensor.moisture_read()
        # read temperature from the temperature sensor
        soil_temp = sensor.get_temp()
        moisutures.append(soil_moisture)
        temps.append(soil_temp)
    return moisutures, temps

def print_data(sensor):
    # read soil mosisture
    soil_moisture = sensor.moisture_read()
    # read temperature from the temperature sensor
    soil_temp = sensor.get_temp()
    print("Soil temp: " + str(soil_temp) + "  Soil moisture: " + str(soil_moisture))
    return

def upload_data_to_sensor_table(moisture_data):
    sensor_names = ["MOISTURE", "SOILTEMP"]
    for i, data in enumerate(moisture_data):
        for sensor_name, values in zip(sensor_names, data):
            upload_data(i, sensor_name, values)

#TODO: Figure out how to assign mulitple sensor addresses
def main():
    addrresses = ["0x36"]
    moisture_sensors = moisture_setup(addrresses)
    moisture_data  = collect_data(moisture_sensors)
    upload_data_to_sensor_table(moisture_data)

if __name__ == "__main__":
    main()
