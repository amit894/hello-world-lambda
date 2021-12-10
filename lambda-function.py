import json
from client import get_content


print('Loading function')


def lambda_handler(event, context):
    get_content(event["url"])
    #print("Received event: " + json.dumps(event))
    return ("Lamba Handler Execution Completed")
