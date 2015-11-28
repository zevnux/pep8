#: SPACE ERROR TEST
for a  in 'abc':
    for b in 'xyz':  # indented with 4 spaces
         print b  # SPACE ERROR: 8 SPACES indentation expected; indentation was 9 spaces
		
		
for a  in 'abc':
    for b in 'xyz':  # indented with 4 spaces
		print b  # SPACE ERROR: 8 spaces indentation expected; indentation was 2 tabs and 0 spaces
