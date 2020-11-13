#!/usr/bin/python
"""System to test all sensors and print outputs
"""
import sys
sys.path.append('.')
from data_collection.temp import main as temp_main
from data_collection.temp import temp_setup
from data_collection.light import main as light_main
from data_collection.light import light_setup
#from data_collection.wind import *
from time import sleep

def main():
    light_sensor = light_setup()
    temp_sensor = temp_setup()
    # put code for adc wind sensor here
#    while True:
    for i in range(10):
        try:
            light_main(light_sensor)
            temp_main(temp_sensor)
            # put adc wind sensor code here
            sleep(2)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
