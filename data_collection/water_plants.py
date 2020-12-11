import sys
sys.path.append('.')
import time
from time import sleep
from data_collection.valve import setup_valve, open_valve, close_valve
from data_collection.pump import setup_pump, run_pump_forward, run_pump_backward, stop_pump
from data_collection.moisture import is_water_safe

def water_plant(plant_id, water_duration=10):
    """plant_id = '1', '2', '3' or '0' or None to loop through all plants"""

    plant_id_to_pins = {
        '1': (26, 23, 24, 0x36),
        '2': (13, 23, 24, 0x37),
        '3': (14, 23, 24, 0x39)
    }

#    ids_to_water = [plant_id] if plant_id != 0 else plant_id_to_pins.keys()
    ids_to_water = [plant_id] if (plant_id is not None) and (plant_id != 0) else plant_id_to_pins.keys()
    try:
        for p_id in ids_to_water:
            print(f"Water plant {p_id}")
            valve_pin, pump_in1, pump_in2, water_address = plant_id_to_pins[p_id]

            # setup
            setup_valve(valve_pin)
            setup_pump(pump_in1, pump_in2)

            # do watering
            start_time = time.time()
            while time.time() - start_time < water_duration and is_water_safe(water_address):
                run_pump_forward(pump_in1, pump_in2, 0.5)
                open_valve(valve_pin, 0.5)

            # stop watering
            print("Soil wet enough")
            close_valve(valve_pin, 1)
            stop_pump(pump_in1, pump_in2, 1)
            sleep(10)
    except KeyboardInterrupt:
        # stop watering
        close_valve(valve_pin, 1)
        stop_pump(pump_in1, pump_in2, 1)


def aerate_water(aerate_duration=60):

    valve_pin, pump_in1, pump_in2 = 26, 23, 24
    # setup
    setup_valve(valve_pin)
    setup_pump(pump_in1, pump_in2)

    # do aeration
    open_valve(valve_pin, 0.5)
    run_pump_backward(pump_in1, pump_in2, 0.5)
    sleep(aerate_duration)

    # stop aerating
    stop_pump(pump_in1, pump_in2, 1)
    close_valve(valve_pin, 1)
    sleep(10)


if __name__ == "__main__":
#    aerate_water()
#    water_plant('1')
    water_plant('2')
#    water_plant('3')

