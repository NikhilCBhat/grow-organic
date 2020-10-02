import boto3

def get_events_table():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table('Events')