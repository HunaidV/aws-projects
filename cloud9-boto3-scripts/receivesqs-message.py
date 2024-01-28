import boto3
import json
import requests
from botocore.exceptions import ClientError

sqs_client = boto3.client("sqs")

def receive_message():
    response = sqs_client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/XXXXXX/boto3messagesqs', #change your QueueURL
        MaxNumberOfMessages=3,
        WaitTimeSeconds=10,
    )
    print(f"Number of messages received: {len(response.get('Messages', []))}")

    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {json.loads(message_body)}")
        print(f"Receipt Handle: {message['ReceiptHandle']}")
        