import keys
import oauth2 as oauth
import json

consumer = oauth.Consumer(keys.global_consumerkey, keys.global_consumersecret)
token = oauth.Token(keys.global_accesstoken, keys.global_tokensecret)
client = oauth.Client(consumer, token)

def GetListMembers(screen_name, slug):
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
		memberlist.add(u.get(u'screen_name'))
	
	return memberlist

#And here’s how you make a POST call:
#import urllib
#response, content = myclient.request("http://someservice.com/api/something/", \
#    method="POST", body=urllib.urlencode({'name': 'value', 'another_name': 'another value'})
