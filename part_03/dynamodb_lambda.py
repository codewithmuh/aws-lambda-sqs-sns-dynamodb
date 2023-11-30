import boto3
import json
from datetime import datetime

## Call the dynamodb resource and the table name
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("DateTime-Table")

## Start of lambda function
def lambda_handler(event, context):
    
## Create a variable of the sns message event 
    snsmsg = event['Records'][0]['Sns']['Message']
    msgid = id(snsmsg)

## Create of variable of the current date and time 
    now = datetime.now()
    date = now.strftime("%H:%M:%S %m/%d/%Y")

## Puts the items into the DyanmoDB table    
    response = table.put_item(
           Item={'ID': msgid, 
           'DateTime': date, 
           'SnsMessage': snsmsg})
    
    
    

# source: youtube.com/@codewithmuh 
# Email: codewithmuh@gmail.com     