import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

response = table.query(
    KeyConditionExpression=Key('StudentID').eq('001')
)

for item in response['Items']:
    print(item)