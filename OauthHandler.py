import keys
import oauth2 as oauth
import json
import urllib
import urlparse

consumer_key = keys.consumerkey
consumer_secret = keys.consumersecret
access_token = ''
access_token_secret = ''

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)
token = None


# Authorize User
def authorize():
	"""Three-legged authentication (for one-time use). Return true/false """
	# CLI Three-Legged Auth code from tutorial by simplegeo from his 'python-oauth2' repo on github
	
	global client
	global token
	
	request_token_url = 'http://twitter.com/oauth/request_token'
	access_token_url = 'http://twitter.com/oauth/access_token'
	authorize_url = 'http://twitter.com/oauth/authorize'
	
	resp, content = client.request(request_token_url, "GET")
	if resp['status'] != '200':
		raise Exception("Invalid response %s." % resp['status'])
	
	request_token = dict(urlparse.parse_qsl(content))
	
	print "Go to the following link in your browser:"
	print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
	print 
	
	oauth_verifier = raw_input('What is the PIN? ')
	
	token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)
	client = oauth.Client(consumer, token)

	resp, content = client.request(access_token_url, "POST")
	access_token = dict(urlparse.parse_qsl(content))
	
	try:
		oauth_token = access_token['oauth_token']
		oauth_token_secret = access_token['oauth_token_secret']
	except:
		print 'An error may have occurred. Retry.'
		return False
	
	f = open('access.twt', 'w')
	f.flush()
	f.write('oauth_token:'+ oauth_token + ';')
	f.write('oauth_token_secret:'+ oauth_token_secret + ';')
	f.close()
	
	return True


def init():
	"""Initialization of Auth variables"""
	
	global client
	global token
	
	# Code to read Access Token from file here:
	try:
		f = open('access.twt', 'r')
		s = f.read()
	
		key_value_pairs = s.split(';')	
		access_token = key_value_pairs[0].split(':')[1]
		access_token_secret = key_value_pairs[1].split(':')[1]
	
		f.close()
	
		token = oauth.Token(access_token, access_token_secret)
		client = oauth.Client(consumer, token)
	
		return True
		
	except:
		return False


# Get List Members
def getlistmembers(screen_name, slug):
	"""Returns members in the given twi-list as list"""

	############# ALGO ##################
	# JSON response format:
	# l = list(response)
	# l[0] is the header, l[1] is the body string
	# 
	# using a JSONDecoder j
	# Dictionary object dictn = j.decode(l[1])
	# 
	# 'dictn' contains a key: u'users', whose value is a list
	# users = dictn.get(u'users')
	# foreach user u
	# 	add screen_name to list

	apistr = 'https://api.twitter.com/1/lists/members.json?slug=' + slug + '&owner_screen_name=' + screen_name + '&cursor=-1'
	response = client.request(apistr)
	
	j = json.JSONDecoder()
	dictn = j.decode(list(response)[1])
	users = dictn.get(u'users')
	
	memberlist = list()
	
	for u in users:
		memberlist.append(u.get(u'screen_name'))
	
	return memberlist


# Add List Members
def addlistmembers(target, users):
	"""Adds all users in argument 'users' as members of twi-list given by 'target' """
	
	# Prepare strings for use in POST body
	userstr = ''
	for u in users:
		userstr = userstr + ',' + u
	
	targetlist = target.split('/')
	owner_screen_name = targetlist[0]
	slug = targetlist[1]
	
	# API url
	apiurl = "https://api.twitter.com/1/lists/members/create_all.json"
	b = urllib.urlencode({'screen_name': userstr, 'owner_screen_name': owner_screen_name, 'slug': slug})
	response, content = client.request(apiurl, method="POST", body=b)
	
	return response, content

