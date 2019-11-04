import sys

total = ""
for arg in sys.argv:
	if arg != sys.argv[0]:
		total += " " + arg
print(''.join(reversed(total))[: -1].swapcase())