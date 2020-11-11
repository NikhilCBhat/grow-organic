#!/usr/bin/python
"""Grow Organic hardware control
Reads sensor values and responds with
running the pump and controlling outlets
"""
import RPi.GPIO as GPIO
from threading import Thread
import pump #import main
import adc #import main
#from light import *
from temp import *
import relay #import main
#from wind import *
#from moisture import *

#pump1 = 24
#pump2 = 23
#relay = 26

# setup functions
#setup_pump(pump1, pump2)
#setup_adc()
#setup_temp()
#setup_light()
#setup_relay(relay)
#calibrate_wind()
#calibrate_moisture()
#data_type() # This probably needs to be called after data setup

# TODO: add multithreading to allow simultaneous action
#[chan0, chan1, chan2, chan3] = data_adc(1)
#[temp, humidity] = data_temp(3)
#[vis, IR, uvIndex] = data_light(3)
#run_pump(pump1, pump2, 10)
#stop_pump(pump1, pump2, 5)
#close_relay(26, 10)
#open_relay(26, 5)

#TODO: Write all the gathered data to database
t_pump = Thread(target=pump, args=())
t_adc = Thread(target=adc, args=())
t_relay = Thread(target=relay, args=())
#t_light = Thread(target=light, args=())
#t_temp = Thread(target=temp, args=())

t_pump.start()
t_adc.start()
t_relay.start()
#t_light.start()
#t_temp.start()

t_pump.join()
t_adc.join()
t_relay.join()
#t_light.join()
#t_temp.join()



#GPIO.cleanup()

