import json  # Import json for handling JSON data
import boto3  # Import boto3 to work with AWS services
from datetime import datetime  # Import datetime to work with dates and times

# Start of function
def lambda_handler(event, context):
    # Creating a variable for the current date and time
    now = datetime.now()

    # Formatting the date and time to display in a specific format
    time_date = now.strftime("%H:%M:%S %m/%d/%Y")

    # Initializing the SQS client
    sqs = boto3.client('sqs')
    
    # Sending a message to the specified SQS queue
    # Replace the QueueUrl with your actual SQS queue URL
    sqs.send_message(
        QueueUrl="https://queue.amazonaws.com/************/your-queue-name-here",
        MessageBody=time_date
    )
    
    # Return a success message indicating the Lambda execution was successful
    return {
        'statusCode': 200,
        'body': json.dumps('The message was sent successfully.')
    }

    
# source: youtube.com/@codewithmuh 
# Email: codewithmuh@gmail.com   
    
    
    
