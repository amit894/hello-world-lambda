import tweepy
from tweepy import OAuthHandler
from secret_client import get_secret


def send_tweet(body):
    consumer_key = get_secret('consumer_key ')
    consumer_secret = get_secret('consumer_secret ')
    access_token = get_secret('access_token')
    access_token_secret = get_secret('access_token_secret ')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(status=body)

send_tweet("Yo Yo Honey Singh Testing")
