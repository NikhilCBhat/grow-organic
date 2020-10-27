import boto3

def get_sensors_table():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table('SensorData')