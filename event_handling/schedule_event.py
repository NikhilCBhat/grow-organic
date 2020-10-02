import argparse
import boto3

from time_utils import parse_date, get_current_utc_time

allowed_event_types = {
    "WATER", "AERATE"
}

def schedule_event(event_type, date, frequency):
    if event_type not in allowed_event_types:
        print(f"Invalid event type: {event_type} must be one of: {allowed_event_types}")

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Events')
    item_dict = {"EventID": get_current_utc_time(), "EventType": event_type, "Date": parse_date(date)}
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
