#!/usr/bin/env python3
"""Test sensor connections and upload data to database
"""
import sys
sys.path.append('.')
from data_collection.temp import main as temp_main
from data_collection.temp import temp_setup
from data_collection.light import main as light_main
from data_collection.light import light_setup
from data_collection.moisture import main as moisture_main
from data_collection.moisture import moisture_setup
#from data_collection.wind import *
from time import sleep

def main():
    addresses = [0x37]
    moisture_sensors = moisture_setup(addresses)
    light_sensor = light_setup()
    temp_sensor = temp_setup()
    # put code for adc wind sensor here

#    while True:
    for i in range(5):
        try:
            light_main(light_sensor)
            temp_main(temp_sensor)
            moisture_main(moisture_sensors)
            # put adc wind sensor code here
            sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
