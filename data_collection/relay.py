#!/usr/bin/env python3
"""Relay setup and control functions
Allows for control of AC outlets
Source: https://electronicshobbyists.com/controlling-ac-devices-with-raspberry-pi-raspberry-pi-relay-control/
"""

import sys
sys.path.append('.')
import RPi.GPIO as GPIO
import time
from time import sleep
from data_collection.light import is_light_safe

wind_pin = 27
light_pin = 17

def setup_relay(relay_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, 1)
    return

def close_relay(relay_pin, run_time):
    GPIO.output(relay_pin, 0)
#    print("Relay closed - Outlet on")
    sleep(run_time)
    return

def open_relay(relay_pin, run_time):
    GPIO.output(relay_pin, 1)
#    print("Relay open - Outlet off")
    sleep(run_time)
    return

def turn_fan_on(wind_duration=10):
    setup_relay(wind_pin)
    start_time = time.time()
    while time.time() - start_time < wind_duration:
        close_relay(wind_pin, 0.5)
    open_relay(wind_pin, 1)
    print("Fan off")

def turn_fan_off():
    setup_relay(wind_pin)
    close_relay(wind_pin, 0.5)

def turn_light_on(light_duration=10):
    setup_relay(light_pin)
    start_time = time.time()
    while time.time() - start_time < light_duration and is_light_safe():
        close_relay(light_pin, 0.5)
    open_relay(light_pin, 1)
    print("Light off")

def turn_light_off():
    setup_relay(light_pin)
    close_relay(light_pin, 0.5)

def main():
    relay_pin1 = 27
    relay_pin2 = 17
    setup_relay(relay_pin1)
    setup_relay(relay_pin2)
    open_relay(relay_pin1, 1)
    open_relay(relay_pin2, 1)

if __name__ == "__main__":
    main()
