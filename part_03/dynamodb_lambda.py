import boto3
import json
from datetime import datetime

# Initialize the DynamoDB resource and define the table name
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("DateTime-Table")

# Lambda function starts here
def lambda_handler(event, context):
    
    # Extract the SNS message from the event
    snsmsg = event['Records'][0]['Sns']['Message']
    msgid = id(snsmsg)  # Generate a unique ID for the message

    # Get the current date and time
    now = datetime.now()
    date = now.strftime("%H:%M:%S %m/%d/%Y")

    # Insert items into the DynamoDB table
    response = table.put_item(
        Item={
            'ID': msgid,
            'DateTime': date,
            'SnsMessage': snsmsg
        }
    )


# source: youtube.com/@codewithmuh 
# Email: codewithmuh@gmail.com     