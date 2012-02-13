import OauthHandler
import sys

# ListEX functions
def get_all_list_members(set_of_twilists):
	"""Returns SET of all members followed by all twi-lists in 'set_of_twilists' """
	
	all_members_set = set()
	
	for l in set_of_twilists:		
		params = l.split('/')
		list_members = OauthHandler.getlistmembers(params[0], params[1])
		all_members_set.union(list_members)
		del list_members
	
	return all_members_set


def copy_lists(target_name, from_lists):
	"""Copies the members of the twi-lists in 'from_lists' to twi-list given by argument 'target_name' """
	
	# Make a list with "target_name" as member # TEMP
	target_list = list()
	target_list.append(target_name)
	
	# Get sets of people already in list (targetname) and in the set of lists to be copied from(from_lists)
	existing_members = get_all_list_members(target_list)
	to_be_members = get_all_list_members(from_lists)
	
	# Make final list of people to be newly added to list
	# SET DIFFERENCE
	to_be_members.difference(existing_members)
	
	# POST to twitter
	OauthHandler.addlistmembers(target_name, list(to_be_members))
	
	del target_list, existing_members, to_be_members	
	return True


def copy_members(target_name, member_list):
	"""Copies the members from 'member_list' to twi-list given by argument 'target_name' """
	OauthHandler.addlistmembers(target_name, member_list)


def entry_check(argv):
	"""Performs a few entry checks/actions including: 
		(1) Prints help/usage if no arguments,
		(2) New authentication if switch is activated,
		(3) Fetches previously validated keys
	"""
	
	usage = "help here"
	
	if ( len(argv) == 1):
		print usage
		return False
		
	elif (sys.argv[1] == "-a"):
		return OauthHandler.authenticate()	
		
	else:
		return True


############################################################################################

def main():
	
	proceed = entry_check(sys.argv)
	
	if(proceed):
		# Process input
		target_name = sys.argv[1]
	
		mem_list = list()
		twilists = list()
	
		# Read all other arguments
		for i in range(2, len(sys.argv)):
			if( sys.argv[i].find('/') == -1 ):
				mem_list.append(sys.argv[i])
			else:
				twilists.append(sys.argv[i])
	
		copy_lists(target_name, twilists)
		copy_members(target_name, mem_list)
	
		del mem_list, twilists

	return True

if __name__ == "__main__":
	main()
