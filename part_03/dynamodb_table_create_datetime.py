
import boto3

##Get the service resource.                        ##Set appropriate region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

##Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='DateTime-Table',
    KeySchema=[
        {
            'AttributeName': 'DateTime',
            'KeyType': 'HASH'  ##Partition key
        },
        {
            'AttributeName': 'ID',
            'KeyType': 'RANGE'  ##Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'DateTime',
            'AttributeType': 'S'  ##S is for string attribute
        },
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'  ##N is for number attibute
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
print("Table status:", table.table_status) ##print table status





# source: youtube.com/@codewithmuh 
# Email: codewithmuh@gmail.com 