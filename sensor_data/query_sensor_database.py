import boto3
from sensor_data.dynamo_utils_sensors import get_sensors_table
from boto3.dynamodb.conditions import Key, Attr
import pdb
from sensor_data.upload_sensor_data import allowed_sensor_types

def get_data_from_database():
    table = get_sensors_table()
    sensorData =[]
    for sensor_type in allowed_sensor_types:
        response = table.scan(FilterExpression=Attr('SensorType').eq(sensor_type))
        sensorData.append({
            "name":sensor_type,
            "timestamps": [float(x['SensorDataID']) for x in response['Items']],
            "values":[float(x['SensorValue']) for x in response['Items']],
        })
    return sensorData


if __name__ == "__main__":
    print(get_data_from_database())