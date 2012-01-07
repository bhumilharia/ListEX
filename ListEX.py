import OauthHandler

# ListEX functions

def GetListMembers(set_of_twilists):
	"""Returns set of all members followed by all lists in set_of_twilists"""
	
	all_members_set = set()
	
	for l in set_of_twilists:
		# Get the JSON response from Twitter for list 'l'
		# 
		# JSON twitter response format for users in a list is:
		# 
		# 

		list_members_json = oauth_req(
			'http://api.twitter.com/1/statuses/home_timeline.json',
			'abcdefg',
			'hijklmnop'
			)
		print "Members IDs from List '", l, "'identified"		
		
		#parse list_members_json here: DeJSONify and convert to set
		
		# Add to Set to be returned
		this_list_members = list_members_json
		all_members_set.union(this_list_members)		
		this_list_members.clear()
	
	return all_members_set

def CopyList(target_name, srclists_set):
	"""Copies the members of the lists in srclists_set to target_name"""
	tgtlist_set = set()
	tgtlist_set.add(target_name)
	
	# Get sets of people already in list (targetname) and in the set of lists to be copied from(srclists_sets)
	target_members_set = GetListMembers(tgtlist_set)
	src_members_set = GetListMembers(srclists_set)
	
	# Make final list of people to be added to list
	src_members_set.difference(target_members_set)
	
	# POST src_members to twitter
	# OR
	# for mem in src_members_set:
	#	POST mem to twitter

	print "Successful"

############################################################################################

def MainProgram():
	
	# read inputs
	# convert into needed format

	return True

