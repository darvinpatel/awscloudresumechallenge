import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresumeaws')

def lambda_handler(event, context):
    try:
        # Retrieve the current count from the DynamoDB table
        response = table.get_item(Key={'id': 'visits'})
        count = response['Item']['count']
        
        # Increment the count
        new_count = count + 1
        
        # Update the count in the DynamoDB table
        table.update_item(
            Key={'id': 'visits'},
            UpdateExpression='SET #c = :val1',
            ExpressionAttributeNames={'#c': 'count'},
            ExpressionAttributeValues={':val1': new_count}
        )
        
        return {
            'statusCode': 200,
            'body': str(new_count)
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
