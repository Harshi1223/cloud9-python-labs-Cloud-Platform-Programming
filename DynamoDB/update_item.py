import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

response = table.update_item(
    Key={'StudentID': '001'},
    UpdateExpression="SET Age = :a",
    ExpressionAttributeValues={
        ':a': 22
    },
    ReturnValues="UPDATED_NEW"
)

print("Updated:", response['Attributes'])