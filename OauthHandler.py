import oauth2 as oauth

# OAuth Mumbo Jumbo
def oauth_req(url, key, secret, http_method="GET", post_body=None,http_headers=None):

	consumer = oauth.Consumer(key = global_consumerkey, secret = global_consumersecret)
	token = oauth.Token(key=key, secret=secret)	
	client = oauth.Client(consumer, token)


	# Step 1: Get a request token. This is a temporary token that is used for 
	# having the user authorize an access token and to sign the request to obtain 
	# said access token.

	resp, content = client.request(request_token_url, "GET")
	if resp['status'] != '200':
		raise Exception("Invalid response %s." % resp['status'])

	request_token = dict(urlparse.parse_qsl(content))

	print "Request Token:"
	print "- oauth_token= %s" % request_token['oauth_token']
	print "- oauth_token_secret = %s" % request_token['oauth_token_secret']
	print 

	# Step 2: Redirect to the provider. Since this is a CLI script we do not 
	# redirect. In a web application you would redirect the user to the URL
	# below.

	print "Go to the following link in your browser:"
	print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
	print 

