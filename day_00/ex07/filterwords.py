import sys
import re

def is_digit(n):
   try:
       int(n)
       return True
   except ValueError:
       return  False
if (len(sys.argv) == 3 and is_digit(sys.argv[2]) and int(sys.argv[2]) > 0
	and not re.findall("[0-9]", sys.argv[1])):
	src = re.split("[^a-zA-Z]+",sys.argv[1])
	res = []
	for tmp in src:
		if len(tmp) > int(sys.argv[2]):
			res.append(tmp)
	print(res)
else:
	print("ERROR")