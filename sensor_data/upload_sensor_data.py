import argparse
import boto3
import time
import datetime
from dynamo_utils_sensors import get_sensors_table
# from event_handling.time_utils import get_current_utc_time

allowed_sensor_types = {
    "PH", "MOISTER","IR", "UV", "TEMPERATURE", "WIND", "VISIBLE"
}

numPlants = 4

def get_current_utc_time():
    now = datetime.datetime.utcnow()
    return int((now - datetime.datetime(1970, 1, 1)).total_seconds())

def upload_data(plant_id, sensor_type, sensor_value, extra_params={}):
    if sensor_type not in allowed_sensor_types:
        print(f"Invalid event type: {sensor_type} must be one of: {allowed_sensor_types}")
    if plant_id > numPlants or plant_id < 0:
        print(f"Invalid plant id: {plant_id}")

    table=get_sensors_table()
    item_dict = {"PlantID":plant_id,"SensorDataID": get_current_utc_time(), "SensorType": sensor_type, "SensorValue": sensor_value}

    for key,value in extra_params.items():
        if key not in item_dict:
            item_dict[key] = value

    table.put_item(Item=item_dict)

def mockData():
    upload_data(1,"MOISTER",10)
    # upload_data(1,"SCLLIGHT",12)
    # upload_data(1,"SDALIGHT",13)
    upload_data(1,"TEMPERATURE",100)



if __name__ == "__main__":
    mockData()
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-n", "--plant_id", required=True)
    # parser.add_argument("-t", "--sensor_type", required=True)
    # parser.add_argument("-f", "--sensor_value", required=True)

    # args = parser.parse_args()
    # upload_data(args.event_type.upper(), args.plant_id, args.sensor_type,args.sensor_value)