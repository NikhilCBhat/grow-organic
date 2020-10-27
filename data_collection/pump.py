#!/usr/bin/python
"""Pump setup and control functions
"""

import RPi.GPIO as GPIO          
from time import sleep

def setup_pump (in1, in2):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    return

# run the pump forwards for specified time
def run_pump (in1, in2, run_time):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    sleep(run_time)
    return

# stop the pump for specified time
def stop_pump (in1, in2, stop_time):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    sleep(stop_time)
    return
