#!/usr/bin/env python3
"""Test sensor connections and upload data to database

Arguments:
   -l/--limit    Limit data collected
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
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--limit", type=int, default=0,
	help="limit data collected, default to loop infinitely")
args = vars(ap.parse_args())

def main(limit):
    addresses = [0x36, 0x37, 0x39]
    moisture_sensors = moisture_setup(addresses)
    light_sensor = light_setup()
    temp_sensor = temp_setup()
    # put code for wind sensor here

    if limit != 0:
        for i in range(limit):
            light_main(light_sensor)
            temp_main(temp_sensor)
            moisture_main(moisture_sensors)
            # put wind sensor code here
            sleep(10)
    else:
        while True:
            light_main(light_sensor)
            temp_main(temp_sensor)
            moisture_main(moisture_sensors)
            # put wind sensor code here
            sleep(10)

if __name__ == "__main__":
    limit = args["limit"]    # limit on number of data points that can be collected
    main(limit)
