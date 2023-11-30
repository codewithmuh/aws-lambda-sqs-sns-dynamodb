# AWS Lambda, SQS, SNS, DynamoDB

## Serverless Architecture with AWS Services

This repository illustrates the implementation of a serverless architecture utilizing various AWS services: AWS Lambda, Amazon SQS, Amazon SNS, Amazon DynamoDB, and Amazon API Gateway. The AWS Command Line Interface (CLI) is utilized for managing these services.

### Overview

In this project, we will create 3 Lambda functions that will:

1. Send a message to the SQS queue when an HTTP API Gateways endpoint is reached.
2. Get the messages from SQS and send them to an SNS topic we have subscribed to by email.
3. Receive the SNS notification and place the message into a DynamoDB table for record keeping.

#### Prerequisites

- AWS account with non-root user and administrative access
- Boto3/AWS CLI/Python3 (at least Python 3.9) installed on your local machine or virtual machine
- Experience with AWS CLI, Python, and AWS Console

For installation and setup:

- [AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Python/Boto3 installation guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
