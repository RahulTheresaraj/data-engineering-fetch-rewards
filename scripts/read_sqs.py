import boto3
import json
from botocore.config import Config
from botocore.exceptions import ClientError

# Configuration
sqs_config = Config(region_name='us-east-1')
queue_url = 'http://localhost:4566/000000000000/login-queue'

def read_from_sqs():
    sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', config=sqs_config, aws_access_key_id='fakeMyKeyId', aws_secret_access_key='fakeSecretAccessKey')
    messages = []
    while True:
        try:
            response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=5)
            sqs_messages = response.get('Messages', [])
            if not sqs_messages:
                break
            for message in sqs_messages:
                receipt_handle = message['ReceiptHandle']
                body = json.loads(message['Body'])
                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
                messages.append(body)
        except ClientError as e:
            if e.response['Error']['Code'] == 'AWS.SimpleQueueService.NonExistentQueue':
                print("Queue does not exist.")
            else:
                print("Error:", e)
            break
    return messages

if __name__ == "__main__":
    messages = read_from_sqs()
    print(json.dumps(messages))  # Send output to next script
