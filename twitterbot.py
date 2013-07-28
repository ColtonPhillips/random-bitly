from random import randrange

# Twitter Bitly Bot
import tweepy

from short import random_bitly

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
    title = soup.title.getText()[:100]

    if randrang(1,6) == 1:
        bot.update_status(random_url('{title} - {url}'.format(title=title, url=url)))
    else:
        bot.update_status(random_url("{title} - You'll never know".format(title=title)))

if __name__=='__main__':
    main()
