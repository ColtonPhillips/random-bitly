# Short URL generator
import string
import random
from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError

# Create bitly address
def id_generator(size=6, chars=string.ascii_letters + string.digits):
	return 'http://bit.ly/'+''.join(random.choice(chars) for x in range(size))

# Find valid bitly address
def random_bitly():
    while True:
        try:
            url = id_generator()
            urlopen(url)
            break
        except (HTTPError, URLError):
            pass
    return  url

