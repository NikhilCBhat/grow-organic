import argparse
import boto3
import time

def parse_date(date):
    return time.mktime(time.strptime(date, "%m/%d/%Y %H:%M"))*1000

def schedule_event(event_type, date, frequency):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Events')
    item_dict = {"EventID": table.item_count, "Date": parse_date(date)}
    if frequency is not None:
        item_dict["Frequency"] = frequency

    table.put_item(
        Item=item_dict
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--event_type", required=True)
    parser.add_argument("-d", "--date", required=True)
    parser.add_argument("-f", "--frequency", required=False)

    args = parser.parse_args()
    schedule_event(args.event_type, args.date, args.frequency)
