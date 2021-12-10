import json
from client import send_tweet


print('Loading function')


def lambda_handler(event, context):
    get_content(event["body"])
    #print("Received event: " + json.dumps(event))
    return ("Lamba Handler Execution Completed")
