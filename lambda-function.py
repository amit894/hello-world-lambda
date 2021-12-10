import json

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    return ("Lamba Handler Execution Completed")
