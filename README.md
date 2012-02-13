ListEX is a script for managing bulk Twitter List operations better.

I primarily made this because a user may have a list that serves the same purpose as lists of many others. Trying to add each member from each list is both time-consuming and tedious.
This script automatically adds everyone from every list (or even individual users) given as input to the desired list


Usage:

	1. Giving no arguments lists help and usage information (currently prints "help here")
		$ python ListEx.py
	
	2. For (one-time) authentication, use:
		$ python ListEx.py -auth
	
	3. For normal usage (if the ont-time authentication has been done before)
		$ python ListEx.py [target_list_name] [users or lists separated by spaces]
	
		IMPORTANT: Lists are specified as username/list_slug
	
		Example:
		$ python ListEx.py bhumilharia/vjti Sengupta/VJTI ankitdaf parascal ankitdaf/VJTI
		

Psst:
	@ankitdaf helped (directed) me wrt command-line arguments.
	Not to mention the saviour author of the (only) amazing page on OAuth I found: http://parand.com/say/index.php/2010/06/13/using-python-oauth2-to-access-oauth-protected-resources/


Wishlist:
- Add feature to remove user(s) from lists
- Facebook list management
