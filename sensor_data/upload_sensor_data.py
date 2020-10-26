import argparse
import boto3
import time
import datetime

allowed_sensor_types = {
    "PH", "MOISTER","LIGHT"
}

numPlants = 4

def upload_data(plant_id, sensor_type, sensor_value):
    if event_type not in allowed_event_types:
        print(f"Invalid event type: {sensor_type} must be one of: {allowed_sensor_types}")
    if plant_id > numPlants || plant_id < 0
        print(f"Invalid plant id: {plant_id}")

    table=get_sensors_table()
    item_dict = {"PlantID":plant_id,"SensorDataID": get_current_utc_time(), "SensorType": sensor_type, "SensorValue": sensor_value}

    for key,value in extra_params.items():
        if key not in item_dict:
            item_dict[key] = value

    table.put_item(Item=item_dict)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--plant_id", required=True)
    parser.add_argument("-t", "--sensor_type", required=True)
    parser.add_argument("-f", "--sensor_value", required=True)

    args = parser.parse_args()
    upload_data(args.event_type.upper(), args.plant_id, args.sensor_type,args.sensor_value)