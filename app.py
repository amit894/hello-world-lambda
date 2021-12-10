import json
import boto3
import base64
import json
import tweepy
from tweepy import OAuthHandler
from botocore.exceptions import ClientError


print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    send_tweet(event["body"])
    return ("Lamba Handler Execution Completed")

def get_secret(key):

    secret_name = "lambda-secrets"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret_string=json.loads(get_secret_value_response['SecretString'])
        return(secret_string[key])
    except ClientError as e:
        print(e)

def send_tweet(body):
    consumer_key = get_secret('consumer_key ')
    consumer_secret = get_secret('consumer_secret ')
    access_token = get_secret('access_token')
    access_token_secret = get_secret('access_token_secret ')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(status=body)
