import boto3

# Get the DynamoDB service resource and specify the region as 'us-east-1'
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Create a DynamoDB table.
table = dynamodb.create_table(
    TableName='DateTime-Table',
    KeySchema=[
        {
            'AttributeName': 'DateTime',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'ID',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'DateTime',
            'AttributeType': 'S'  # 'S' denotes a string attribute
        },
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'  # 'N' denotes a number attribute
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,   # Number of read capacity units provisioned
        'WriteCapacityUnits': 10   # Number of write capacity units provisioned
    }
)

print("Table status:", table.table_status)  # Print the table status
