import boto3  # Import boto3 for AWS services interaction

# Call the SNS client and specify the AWS region
sns = boto3.client("sns", region_name="your-region-0")  # Change 'your-region-0' to your desired AWS region

# Create a variable for the topic created with 'response' 
# Adding the response to the topic_arn variable to print out the TopicArn
response = sns.create_topic(Name="Project15_sns")
topic_arn = response["TopicArn"]

# Print the ARN of the created topic
print("Topic ARN:", topic_arn)

# Subscribe to an email. TopicArn, Protocol, and Endpoint are required.
# Pulling the SubscriptionArn from the results dictionary upon successful subscription
# It will show as "pending confirmation" until confirmed
sub = sns.subscribe(
    TopicArn=topic_arn,
    Protocol="email",
    Endpoint="youremailaddress@here.com"  # Replace this with your email address
)

# Place the "pending confirmation" into a "pending" variable with the result of the "sub" variable
# Then print the result with a message and the "pending" variable
pending = sub["SubscriptionArn"]
print("Email subscribed:", pending)




# source: youtube.com/@codewithmuh 
# Email: codewithmuh@gmail.com 