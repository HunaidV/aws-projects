import boto3 
import json
import requests
from botocore.exceptions import ClientError

#DelaySeconds: Messages are delayed by this value before being delivered.
#RedrivePolicy: Specifies the dead-letter queue functionality
#VisibilityTimeout: Visibility timeout for the queue in seconds. This is the period of time where a particular message is only visible to a single consumer.
sqs_client = boto3.client("sqs")

def create_queue():
    sqs_response = sqs_client.create_queue(
        QueueName="boto3messagesqs", 
        Attributes={
            "DelaySeconds":"0", 
            "VisibilityTimeout": "60"})
    print(sqs_response)


    
def get_queue_url():
    sqs_response = sqs_client.get_queue_url(QueueName="boto3messagesqs")
    return sqs_response["QueueUrl"]


value = input("Please enter your message for Hunaid!\n")



def send_message():
    message = {"Hunaid": value}
    sqs_response = sqs_client.send_message(
        QueueUrl=get_queue_url(),
        MessageBody=json.dumps(message)
    ) 
    return sqs_response

print(send_message())