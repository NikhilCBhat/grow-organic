#!/usr/bin/python
"""Grow Organic hardware control
Reads sensor values and responds with
running the pump and controlling outlets
"""
import RPi.GPIO as GPIO
from pump import *
from adc import *
from light import *
from temp import *
from relay import *
from wind import *
from moisture import *

pump1 = 24
pump2 = 23
relay = 26

# setup functions 
setup_pump(pump1, pump2)
setup_adc()
setup_temp()
setup_light()
setup_relay(relay)
calibrate_wind()
calibrate_moisture()
data_type() # This probably needs to be called after data setup

# TODO: add multithreading to allow simultaneous action
[chan0, chan1, chan2, chan3] = data_adc(1)
[temp, humidity] = data_temp(3)
[vis, IR, uvIndex] = data_light(3)
run_pump(pump1, pump2, 10)
stop_pump(pump1, pump2, 5)
close_relay(26, 10)
open_relay(26, 5)

#TODO: Write all the gathered data to database 

GPIO.cleanup()

