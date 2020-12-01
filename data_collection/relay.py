#!/usr/bin/env python3
"""Relay setup and control functions
Allows for control of AC outlets
Source: https://electronicshobbyists.com/controlling-ac-devices-with-raspberry-pi-raspberry-pi-relay-control/
"""

import RPi.GPIO as GPIO
import time
from time import sleep
wind_pin = 27
light_pin = 17
from data_collection.light import is_light_safe

def setup_relay(relay_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, 1)
    return

def close_relay(relay_pin, run_time):
    GPIO.output(relay_pin, 0)
    print("Relay closed - Outlet on")
    sleep(run_time)
    return

def open_relay(relay_pin, run_time):
    GPIO.output(relay_pin, 1)
    print("Relay open - Outlet off")
    sleep(run_time)
    return

def turn_fan_on(wind_duration=60):
    setup_relay(wind_pin)
    start_time = time.time()
    while time.time() - start_time() < wind_duration:
        close_relay(wind_pin, 0.5)
    open_relay(wind_pin, 1)

def turn_light_on(light_duration=60):
    setup_relay(light_pin)
    start_time = time.time()
    while time.time() - start_time() < light_duration and is_light_safe():
        close_relay(light_pin, 0.5)
    open_relay(light_pin, 1)

def main():
    relay_pin1 = 27
    relay_pin2 = 17
    setup_relay(relay_pin1)
    setup_relay(relay_pin2)
    while True:
        try:
            open_relay(relay_pin1, 5)
            open_relay(relay_pin2, 10)
            close_relay(relay_pin1, 5)
            close_relay(relay_pin2, 10)
        except KeyboardInterrupt:
            open_relay(relay_pin1, 10)
            open_relay(relay_pin2, 10)
            break

if __name__ == "__main__":
    turn_light_on()
    turn_light_off()
