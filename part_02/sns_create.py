import boto3

## Call the sns client and region you are in. Change your region.
sns = boto3.client("sns",
                   region_name="your-region-0")

## Create a variable for when your topic is created with 'response' 
## then adding that response to to the topic_arn variable to print out the TopicArn 
## pulled from the results dictionary in successful run
response = sns.create_topic(Name="Project15_sns")
topic_arn = response["TopicArn"]

## print the ARN of the topic
print(topic_arn)

## Subscribe to email. TopicArn, Protocol and Endpoint are required.
## Pulling the SubscriptionArn from the results dictionary on successful subscribe
## There it will say "pending confirmation"
sub = sns.subscribe(TopicArn=topic_arn,
                    Protocol="email",
                    Endpoint="youremailaddress@here.com")

## Placing the "pending confirmation" into a "pending" variable 
## with the result of the "sub" variable
## Then printing the result with my own message and the "pending" variable
pending = sub["SubscriptionArn"]
print("email subscribed:", (pending))