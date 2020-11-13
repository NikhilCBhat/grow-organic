import sys
sys.path.append('.')

import argparse
import boto3
import time
import datetime
from decimal import Decimal
from sensor_data.dynamo_utils_sensors import get_sensors_table
from event_handling.time_utils import get_current_utc_time
from event_handling.schedule_event import schedule_event
import pandas as pd

allowed_sensor_types = {
    "PH", "MOISTURE","IR", "UV", "TEMPERATURE", "WIND", "VISIBLE", "HUMIDITY"
}

numPlants = 4
 
def create_function(row):

    comparison_to_function = {
        "gt": lambda x, y: x>y,
        "lt": lambda x,y: x<y,
        "eq": lambda x,y: x==y
    }

    def function_to_return(sensor_type, sensor_value):
        comparison_function = comparison_to_function[row["COMPARISON"]]

        if sensor_type == row["SENSOR"] and comparison_function(sensor_value, row["VALUE"]):
            schedule_event(row["EVENT"], time.time(), is_utc_time=True)
    
    return function_to_return


def get_trigger_functions(trigger_file="triggers.csv"):
    df = pd.read_csv(trigger_file)

    return list(df.apply(lambda row: create_function(row) , axis=1))

def upload_data(plant_id, sensor_type, sensor_value, extra_params={}):
    if sensor_type not in allowed_sensor_types:
        print(f"Invalid event type: {sensor_type} must be one of: {allowed_sensor_types}")
        return

    if plant_id > numPlants or plant_id < 0:
        print(f"Invalid plant id: {plant_id}")
        return

    table = get_sensors_table()
    item_dict = {"PlantID":plant_id,"SensorDataID": get_current_utc_time(), "SensorType": sensor_type, "SensorValue": Decimal(str(sensor_value))}

    for key,value in extra_params.items():
        if key not in item_dict:
            item_dict[key] = value

    print("Putting item in table:", item_dict)
    table.put_item(Item=item_dict)

    for f in get_trigger_functions():
        f(sensor_type, sensor_value)

def mockData():
    upload_data(1,"VISIBLE",1)
    upload_data(1,"TEMPERATURE",100)


if __name__ == "__main__":
    mockData()
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-n", "--plant_id", required=True)
    # parser.add_argument("-t", "--sensor_type", required=True)
    # parser.add_argument("-f", "--sensor_value", required=True)

    # args = parser.parse_args()
    # upload_data(args.event_type.upper(), args.plant_id, args.sensor_type,args.sensor_value)
