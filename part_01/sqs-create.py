## Script that creates a Standard SQS Queue

## Import the boto3 client
import boto3

## Get the service resource for SQS
sqs = boto3.resource('sqs')

## Create the queue. This returns an SQS queue. Enter your own desired queue name. 
queue = sqs.create_queue(QueueName='your-queue-name')

## Print the queue url for record
print(queue.url)




# source: youtube.com/@codewithmuh 
# Email: codewithmuh@gmail.com 