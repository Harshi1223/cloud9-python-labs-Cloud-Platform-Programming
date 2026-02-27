import boto3

# Use default Cloud9 credentials
dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Students',
    KeySchema=[
        {
            'AttributeName': 'StudentID',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'StudentID',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.wait_until_exists()
print("Table created successfully!")