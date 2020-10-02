import argparse
import boto3
import time
import datetime

allowed_event_types = {
    "WATER", "AERATE"
}

def parse_date(date):
    return int(time.mktime(time.strptime(date, "%m/%d/%Y %H:%M"))*1000)

def generate_event_id():
    now = datetime.datetime.utcnow()
    return int((now - datetime.datetime(1970, 1, 1)).total_seconds())

def schedule_event(event_type, date, frequency):
    if event_type not in allowed_event_types:
        print(f"Invalid event type: {event_type} must be one of: {allowed_event_types}")

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Events')
    item_dict = {"EventID": generate_event_id(), "EventType": event_type, "Date": parse_date(date)}
    if frequency is not None:
        item_dict["Frequency"] = int(frequency)

    table.put_item(Item=item_dict)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--event_type", required=True)
    parser.add_argument("-d", "--date", required=True)
    parser.add_argument("-f", "--frequency", required=False)

    args = parser.parse_args()
    schedule_event(args.event_type.upper(), args.date, args.frequency)
