import boto3
import base64
from botocore.exceptions import ClientError
import json


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

#get_secret()
