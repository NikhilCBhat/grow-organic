#!/usr/bin/python
"""Relay setup and control functions
Allows for control of AC outlets
Source: https://electronicshobbyists.com/controlling-ac-devices-with-raspberry-pi-raspberry-pi-relay-control/
"""

import RPi.GPIO as GPIO
from time import sleep

def setup_relay(relay_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, 1)
    return

def close_relay(relay_pin, run_time):
#    try:
#        while True:
    GPIO.output(relay_pin, 0)
    print("Relay closed - Outlet on")
    sleep(run_time)
#             GPIO.output(relay_pin, 1)
#             sleep(run_time)
#    except KeyboardInterrupt:
#        pass
#    GPIO.cleanup()
    return

def open_relay(relay_pin, run_time):
#    try:
#        while True:
    GPIO.output(relay_pin, 1)
    print("Relay open - Outlet off")
    sleep(run_time)
#             GPIO.output(relay_pin, 1)
#             sleep(run_time)
#    except KeyboardInterrupt:
#        pass
#    GPIO.cleanup()
    return

def main():
    relay_pin = 26
    setup_relay(relay_pin)
    while True:
        try:
            open_relay(relay_pin, 5)
            close_relay(relay_pin, 5)
        except KeyboardInterrupt:
            open_relay(relay_pin, 10)
            break
    #    upload_data_to_sensor_table(light_data)
    #    sleep(10)

if __name__ == "__main__":
    main()
