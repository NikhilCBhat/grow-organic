import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='SensorData',
    KeySchema=[
        {
            'AttributeName': 'SensorDataID',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'SensorDataID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'PlantID',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='SensorData')
print("Table Exists! Table count: ", table.item_count)