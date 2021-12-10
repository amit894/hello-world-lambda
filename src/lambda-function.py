import json
from twitter_client import send_tweet


print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    send_tweet(event["body"])
    return ("Lamba Handler Execution Completed")
