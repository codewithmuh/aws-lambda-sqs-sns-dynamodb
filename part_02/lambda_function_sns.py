import json  # Import json for JSON data handling
import boto3  # Import boto3 for AWS services interaction

# Calling the SNS boto3 client
client = boto3.client("sns")

# Define your SNS ARN for the topic to which you want to publish messages
snsarn = 'arn:aws:sns:us-east-1:xxxxxxxxxxxx:Project15_sns'  # Replace this with your SNS ARN

# This Lambda function accepts an Amazon SQS record as input and processes it
# The 'payload' variable accepts the record
# Link for more information: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-create-package.html#with-sqs-example-deployment-pkg-python
def lambda_handler(event, context):
    for record in event['Records']:
        print("Processing record...")
        payload = record["body"]
        print(str(payload))

        # Client required to publish to our SNS topic
        response = client.publish(
            TopicArn=snsarn,
            Message=payload
        )

    # Return a message for a successful Lambda execution
    # This message will show up when you test the function
    return {
        'statusCode': 200,
        'body': json.dumps('Message published to SNS successfully')
    }
