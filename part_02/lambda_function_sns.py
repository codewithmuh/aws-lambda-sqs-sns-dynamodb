import json
import boto3

## Calling the sns boto3 client
client = boto3.client("sns")

## created variable for sns arn, it doesnt seem to work 
## when I hardcode it into the TopicArn in the publish section
snsarn = ('arn:aws:sns:us-east-1:xxxxxxxxxxxx:Project15_sns') #<<<replace this with your SNS arn

## Accepts an Amazon SQS record as input and processes 
## it from the other Lambda function then 'payload' variable accepts the record 
## link: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-create-package.html#with-sqs-example-deployment-pkg-python
def lambda_handler(event, context):
    for record in event['Records']:
        print("test")
        payload = record["body"]
        print(str(payload))

## Client required to publish to our sns topic  
    response = client.publish(
                      TopicArn = snsarn,
                      Message = payload)
    
## Return message for successful Lambda execution,
## which will show up when you test the function
    return {
        'statusCode': 200,
        'body': json.dumps('Im triggered again')
    }