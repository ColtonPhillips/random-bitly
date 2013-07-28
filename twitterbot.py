# Twitter Bitly Bot
from short import random_url
import tweepy

consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)
bot = tweepy.API(auth)
bot.update_status(random_url())
