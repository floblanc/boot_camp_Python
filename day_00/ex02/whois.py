import sys

def is_digit(n):
   try:
       int(n)
       return True
   except ValueError:
       return  False

if len(sys.argv) > 2 or (len(sys.argv) == 2
	and is_digit(sys.argv[1]) == False):
	print("ERROR")
elif len(sys.argv) == 2:
	if sys.argv[1] == 0:
		print("I'm Zero")
	elif (int(sys.argv[1]) % 2) == 0:
		print("I'm Even")
	else:
		print("I'm Odd")
