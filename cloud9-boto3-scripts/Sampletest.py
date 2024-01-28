import boto3 
import requests
from botocore.exceptions import ClientError

sqs_client = boto3.client("sqs")

def get_sqs_url():
    response = sqs_client.get_queue_url(QueueName='boto3messagesqs')
    return response

data = get_sqs_url()

for i in range(len(data)):
    print(i)
    
    
