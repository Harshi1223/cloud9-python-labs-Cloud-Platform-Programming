import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

response = table.get_item(
    Key={'StudentID': '001'}
)

print(response['Item'])