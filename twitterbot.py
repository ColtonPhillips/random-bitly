# Twitter Bitly Bot
from bitlify import random_bitly
import tweepy
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
from random import randrange

# Twitter developer account authentication credentials
consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''

def main():
    
    # Sign in to Twitter
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token_key,access_token_secret)
    bot = tweepy.API(auth)
    
    # Get URL and find page title
    url = random_bitly()
    response = urlopen(url).read()
    soup = BeautifulSoup(response)

    # Beat the Twitter spam filter
    if soup.find('title'):
        title = soup.find('title').getText()[:100]
        if randrange(1,3) == 1:
            bot.update_status('{title} - {url}'.format(title=title, url=url))
        else:
            bot.update_status("{title} - You'll never know!".format(title=title))
    else:
        bot.update_status("I don't know... and you'll never know!")


if __name__=='__main__':
    main()
