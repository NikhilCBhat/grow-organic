from time import sleep
from data_collection.valve import setup_valve, open_valve, close_valve
from data_collection.pump import setup_pump, run_pump_forward, stop_pump

def water_plant(plant_id, water_duration):

    plant_id_to_pins = {
        1: (26, 23, 24),
        2: (3, 10, 50)
    }

    ids_to_water = plant_id if plant_id != 0 else plant_id_to_pins.keys()

    for p_id in ids_to_water:
        print(f"Water plant {p_id}")
        valve_pin, pump_in1, pump_in2 = plant_id_to_pins[p_id]

        # setup
        setup_valve(valve_pin)
        setup_pump(pump_in1, pump_in2)

        # do watering
        run_pump_forward(pump_in1, pump_in2, water_duration)
        open_valve(valve_pin, water_duration)

        # stop watering
        close_valve(valve_pin, 1)
        stop_pump(pump_in1, pump_in2, 1)
        sleep(10)

