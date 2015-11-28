#: TAB ERROR TEST
for a in 'abc':
	print "b"  # indented with 1 tab
	for b in 'xyz':  # indented with 1 tab
	     print a  # "TAB ERROR: 2 tabs indentation expected; indentation was 1 tabs and 5 spaces"				