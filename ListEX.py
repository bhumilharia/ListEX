import oauth2 as oauth
import keys
import OauthHandler

# ListEX functions

def GetListMembers(listnames):
	"""Returns list of all members followed by all lists in listnames"""
	all_list_members = ""
	for l in listnames:
		list_members_json = oauth_req(
			'http://api.twitter.com/1/statuses/home_timeline.json',
			'abcdefg',
			'hijklmnop'
			)
		print "Members IDs from List '", l, "'identified"

		#parse list_members_json here
		all_list_members = all_list_members + list_members

	return all_list_members

def CopyList( target_name, source_lists):

	target_members = GetListMembers( target_name )  #convert target_name into a list
	src_members = GetListMembers(source_lists)

	# merge target_members, src_members
	# POST src_members to twitter

	# OR
	# for mem in src_members: 
	#	POST mem to twitter

	print "Successful"

############################################################################################

def MainProgram():
	# read inputs
	# convert into needed format

	return True

