import sys

total = ""
if len(sys.argv) == 1:
	exit()
for arg in sys.argv:
	if arg != sys.argv[0]:
		total += " " + arg
print(''.join(reversed(total))[: -1].swapcase())