#Twitter Bitly Bot
from short import random_bitly
import tweepy
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
from random import randrange

consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''

def main():
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token_key,access_token_secret)
    bot = tweepy.API(auth)
    url = random_bitly()
    response = urlopen(url).read()
    soup = BeautifulSoup(response)
    while True:
        try:
            title = soup.title.getText()[:100]
            break
        except NoneType:
            title = 'Whoops'

    if randrange(1,3) == 1:
        bot.update_status('{title} - {url}'.format(title=title, url=url))
    else:
        bot.update_status("{title} - You'll never know!".format(title=title))

if __name__=='__main__':
    main()
