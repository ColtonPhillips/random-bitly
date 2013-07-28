# Short URL generator
import string
import random
from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError

def id_generator(size=6, chars=string.ascii_letters + string.digits):
	return 'http://bit.ly/'+''.join(random.choice(chars) for x in range(size))

def random_bitly():
    while True:
        try:
            url = id_generator()
            urlopen(url)
            break
        # Round brackets need because python bug... remember that Bert.
        except (HTTPError, URLError):
            pass
    return  url

