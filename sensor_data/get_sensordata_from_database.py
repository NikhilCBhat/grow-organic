import boto3
from dynamo_utils_sensors import get_sensors_table
from boto3.dynamodb.conditions import Key, Attr
import pdb
from upload_sensor_data import allowed_sensor_types

def get_sensor_from_database():
    table = get_sensors_table()
    sensorData =[]
    for theType in allowed_sensor_types:
    response = table.scan(
        FilterExpression=Attr('SensorType').eq(theType)
    )
    sensorData.append({
    "name":theType,
    "timestamps": [float(x['SensorDataID']) for x in response['Items']],
    "values":[float(x['SensorValue']) for x in response['Items']],
    })
    return sensorData


if __name__ == "__main__":
print(get_sensor_from_database())