import argparse
import boto3
import pandas as pd

from event_handling.time_utils import parse_date, get_current_utc_time
from event_handling.dynamo_utils import get_events_table

allowed_event_types = {
    "WATER", "AERATE"
}

def schedule_events_csv(filename):
    table = get_events_table()

    for item in pd.read_csv(filename).to_dict('records'):
        item["EventID"] = get_current_utc_time()
        table.put_item(Item=item)

def schedule_event(event_type, event_time, plant_id=0, frequency=None, is_utc_time=False, is_from_gui=False, extra_params={}):
    if event_type not in allowed_event_types:
        print(f"Invalid event type: {event_type} must be one of: {allowed_event_types}")

    table = get_events_table()
    event_time = int(event_time) if is_utc_time else parse_date(event_time, is_from_gui)
    item_dict = {"EventID": get_current_utc_time(), "EventType": event_type, "EventTime": event_time, "PlantID": plant_id}
    if frequency is not None:
        item_dict["Frequency"] = int(frequency)

    for key,value in extra_params.items():
        if key not in item_dict:
            item_dict[key] = value

    table.put_item(Item=item_dict)
    print(f"Scheduled event {item_dict}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--event_type", required=True)
    parser.add_argument("-d", "--date", required=True)
    parser.add_argument("-f", "--frequency", required=False)

    args = parser.parse_args()
    schedule_event(args.event_type.upper(), args.date, args.frequency)
