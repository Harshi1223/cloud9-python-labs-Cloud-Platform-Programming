import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

table.put_item(
    Item={
        'StudentID': '001',
        'Name': 'Alice',
        'Age': 21,
        'Course': 'Computer Science'
    }
)

print("Item inserted successfully!")