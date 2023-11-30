import boto3  # Import boto3 for AWS services interaction

# Get the service resource for SQS
sqs = boto3.resource('sqs')

# Create an SQS queue. Replace 'your-queue-name' with your desired queue name
queue = sqs.create_queue(QueueName='your-queue-name')

# Print the URL of the created queue for reference
print("Queue URL:", queue.url)


# source: youtube.com/@codewithmuh 
# Email: codewithmuh@gmail.com 