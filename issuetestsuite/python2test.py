#: TAB ERROR TEST
for a in 'abc':
	for b in 'xyz':
	    print a # indented with 5 spaces # "TAB ERROR: TAB INDENTATION EXPECTED; 5 SPACES WERE USED"				
	print b # indented with 4 spaces

#:	SPACE ERROR TEST
for a  in 'abc':
    for b in 'xyz':
	   print a # indented with 3 spaces
			# "SPACE ERROR1: 4 SPACE INDENTATION EXPECTED; 3 SPACES WERE USED"		   
      print b # indented with 6 space
			# "SPACE ERROR1: 4 SPACE INDENTATION EXPECTED; 6 SPACES WERE USED"		  
	print 1   # indented with 1 tab
			# "SPACE ERROR2: 4 SPACE INDENTATION EXPECTED; TAB WAS USED"
			  
			 
			 
#: INDENTATION LEVEL TEST	
def test():
		print "c"  # wrong indentation level
				# "INDENTATION ERROR: WRONG INDENTATION LEVEL"


