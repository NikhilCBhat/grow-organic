#!/usr/bin/env python3
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
def run_pump_forward (in1, in2, run_time):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
#    print("Run forward")
    sleep(run_time)
    return

def run_pump_backward (in1, in2, run_time):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    print("Run backward")
    sleep(run_time)
    return

# stop the pump for specified time
def stop_pump (in1, in2, stop_time):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    print("Pump Stop")
    sleep(stop_time)
    return

def main():
    in1 = 23
    in2 = 24
    stop_time = 2
    run_time = 2
    setup_pump(in1, in2)
    while True:
        try:
#            run_pump_forward(in1, in2, run_time)
            stop_pump(in1, in2, stop_time)
#            run_pump_backward(in1, in2, run_time)
            stop_pump(in1, in2, stop_time)
        except KeyboardInterrupt:
            stop_pump(in1, in2, stop_time)
            break
    return

if __name__ == "__main__":
    main()
