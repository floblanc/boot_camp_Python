import sys

def print_usage():
	print("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")

def is_digit(n):
   try:
       int(n)
       return True
   except ValueError:
       return  False

if len(sys.argv) == 3 and is_digit(sys.argv[1]) and is_digit(sys.argv[2]):
	print("Sum:\t\t" + str(int(sys.argv[1]) + int(sys.argv[2])))
	print("Difference:\t" + str(int(sys.argv[1]) - int(sys.argv[2])))
	print("Product:\t", str(int(sys.argv[1]) * int(sys.argv[2])))
	if int(sys.argv[2]) != 0:
		print("Quotient:\t" + str(int(sys.argv[1]) / int(sys.argv[2])))
		print("Remainder:\t" + str(int(sys.argv[1]) % int(sys.argv[2])))
	else:
		print("Quotient:\tERROR (div by zero)")
		print("Remainder:\tERROR (modulo by zero)")
else:
	if len(sys.argv) > 3:
		print("InputError: too many arguments")
	elif len(sys.argv) < 3 and len(sys.argv) > 1:
		print("InputError: not enought arguments")
	elif len(sys.argv) > 1:
		print("InputError: only numbers")
	print_usage()
