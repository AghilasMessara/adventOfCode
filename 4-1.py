import hashlib
input = """yzbqklnj"""

found = False
i = 0
while (not found):
	i = i + 1
	hash = hashlib.md5(input + str(i)).hexdigest()
	if str(hash).startswith('000000'):
		found = True

if found:
	print """found : %s""", i
else:
	print """Not found :(."""
		
