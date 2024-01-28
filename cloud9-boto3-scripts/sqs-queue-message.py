import boto3 


#DelaySeconds: Messages are delayed by this value before being delivered.
#RedrivePolicy: Specifies the dead-letter queue functionality
#VisibilityTimeout: Visibility timeout for the queue in seconds. This is the period of time where a particular message is only visible to a single consumer.

def create_queue():
    sqs_client = boto3.client("sqs")
    sqs_response = sqs_client.create_queue(
        QueueName="boto3messagesqs", 
        Attributes={
            "DelaySeconds":"0", 
            "VisibilityTimeout": "60"})


    