import boto3
from dynamo_utils import get_events_table
from boto3.dynamodb.conditions import Key, Attr
from time_utils import get_current_utc_time
import pdb
from schedule_event import schedule_event

def water_plants():
    print("Watering the plant!")

def aerate_plants():
    print("Aerating the plant!")

event_type_to_action = {
    "WATER": water_plants,
    "AERATE": aerate_plants
}

def take_action(event):
    event_id = event["EventID"]
    print(f"\nTaking action on: {event_id}")
    event_action = event_type_to_action[event["EventType"]]
    event_action()

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

def perform_all_availible_actions():
    actionable_events = get_actionable_events()
    for event in get_actionable_events():
        take_action(event)

if __name__ == "__main__":
    perform_all_availible_actions()
