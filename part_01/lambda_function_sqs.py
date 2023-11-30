import json ## Import json for the return portion of code
import boto3 ## Import boto3 to work with AWS
from datetime import datetime ## Import datetime so we can get...date and time

## Start of fuction
def lambda_handler(event, context):
    
    ## Creating a variable for the date and time
    now = datetime.now()
    ## Create another variable to take the 'now' 
    ## and place it into the message body as hour, min, second, month, day and year
    time_date = now.strftime("%H:%M:%S %m/%d/%Y")

    ## Calling the SQS client
    sqs = boto3.client('sqs')
    
    ## Sending message to the SQS queue we created
    ## This is where you want to enter the URL we copied down from earlier
    ## that points to your SQS queue
    sqs.send_message(QueueUrl="https://queue.amazonaws.com/************/your-queue-name-here",
    MessageBody=time_date)
    
    ## Return message for successful Lambda execution,
    ## which will show up when you test the function
    return {
        'statusCode': 200,
        'body': json.dumps('Im so triggered right now')
    }
    
    
# source: youtube.com/@codewithmuh 
# Email: codewithmuh@gmail.com   
    
    
    
