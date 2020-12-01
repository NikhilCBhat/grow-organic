#!/usr/bin/env python3
"""Setup, open, and close solenoid valves
"""
import RPi.GPIO as GPIO
from time import sleep

def setup_valve(valve_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(valve_pin, GPIO.OUT)
    GPIO.output(valve_pin, 0)
    return

def open_valve(valve_pin, run_time):
    GPIO.output(valve_pin, 1)
    print("Solenoid Open")
    sleep(run_time)
    return

def close_valve(valve_pin, run_time):
    GPIO.output(valve_pin, 0)
    print("Solenoid Closed")
    sleep(run_time)
    return

def water_plant(valve_pin, water_time):
    setup_valve(valve_pin)
    open_valve(valve_pin, water_time)
    close_valve(valve_pin, 1)

def main():
    valve_pin = 26
    setup_valve(valve_pin)
    while True:
        try:
            open_valve(valve_pin, 5)
            close_valve(valve_pin, 5)
        except KeyboardInterrupt:
            close_valve(valve_pin, 10)
            break

if __name__ == "__main__":
    main()
