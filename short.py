# Short URL generator
import string
import random
from urllib2 import urlopen
from urllib2 import HTTPError

def id_generator(size=6, chars=string.ascii_letters + string.digits):
	return 'http://bit.ly/'+''.join(random.choice(chars) for x in range(size))

def random_url():
	while 1:
		try:
			url = id_generator()
			urlopen(url).code
			break
		except HTTPError:
			pass

	return url

