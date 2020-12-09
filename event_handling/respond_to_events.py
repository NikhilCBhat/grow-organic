import sys
sys.path.append('.')
import boto3
import time
from pprint import pprint
from dynamo_utils import get_events_table
from boto3.dynamodb.conditions import Key, Attr
from time_utils import get_current_utc_time
from schedule_event import schedule_event
from data_collection.water_plants import water_plant, aerate_water
from data_collection.relay import turn_fan_on, turn_light_on, turn_fan_off, turn_light_off

def fan_on(x):
    print("In fan wrapper")
    turn_fan_on()

event_type_to_action = {
    "WATER": water_plant,
    "FAN ON": fan_on,
    "FAN OFF": lambda x: turn_fan_off(),
    "LIGHT ON": lambda x: turn_light_on(),
    "LIGHT OFF": lambda x: turn_light_off(),
    "AERATE": lambda x: aerate_water()
}



def take_action(event):
    event_id = event["EventID"]
    print(f"\nTaking action on: {event_id} with event type {event['EventType']}")
    event_action = event_type_to_action[event["EventType"]]
    event_action(event.get("PlantID", 0))

    if 'Frequency' in event:
        reschedule_event(event)

    remove_event(event)

def reschedule_event(event):
    event_id = event["EventID"]
    print(f"Rescheduling: {event_id}")
    new_event_time = int(event["EventTime"] + event["Frequency"])
    schedule_event(event["EventType"], new_event_time, event["Frequency"], is_utc_time=True)

def remove_event(event):
    event_id = event["EventID"]
    print(f"Removing: {event_id}")
    table = get_events_table()
    table.delete_item(
        Key={
            'EventID': event["EventID"],
        }
    )

def get_actionable_events():

    table = get_events_table()
    response = table.scan(
        FilterExpression=Attr('EventTime').lt(get_current_utc_time()*1000)
    )
    return response['Items']

def perform_all_availible_actions(limit):
    def f():
        actionable_events = get_actionable_events()
        for event in get_actionable_events():
            take_action(event)
        time.sleep(10)

    if limit:
        for _ in range(limit):
            f()
        return

    while True:
        f()


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--limit", type=int, default=0,
        help="limit data collected, default to loop infinitely")
    args = vars(ap.parse_args())
    limit = args["limit"]
    perform_all_availible_actions(limit)
