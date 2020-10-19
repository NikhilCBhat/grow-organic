import argparse
import boto3
import time
import datetime

allowed_sensor_types = {
    "PH", "MOISTER","LIGHT"
}

def upload_data(sensor_type, sensor_value):
    if event_type not in allowed_event_types:
        print(f"Invalid event type: {sensor_type} must be one of: {allowed_sensor_types}")

    table=get_sensors_table()
    item_dict = {"SensorDataID": get_current_utc_time(), "SensorType": sensor_type, "SensorValue": sensor_value}

    table.put_item(Item=item_dict)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--sensor_type", required=True)
    parser.add_argument("-d", "--sensor_value", required=True)

    args = parser.parse_args()
    schedule_event(args.event_type.upper(), args.date, args.frequency)