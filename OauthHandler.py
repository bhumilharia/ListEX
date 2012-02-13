import keys
import oauth2 as oauth
import json
import urllib

consumer = oauth.Consumer(keys.global_consumerkey, keys.global_consumersecret)
token = oauth.Token(keys.global_accesstoken, keys.global_tokensecret)
client = oauth.Client(consumer, token)

# Authenticate User
def authenticate():
	"""Authenticate user before access is granted. Return true/false """
	return True


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

