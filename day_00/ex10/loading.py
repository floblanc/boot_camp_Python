from time import sleep
import sys

def ft_progress(listy):
	for i in listy:
		yield i
max = 1000
t = 0.01
len = 30
listy = range(max)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(t)
	print("ETA: ", "{:.2f}".format((max - elem) * t), "s [ "
	, int(elem * 100 / max), "%][", "=" * int(elem / max * len), ">"
	, " " * int(len - 1 - int(elem / max * len)), "] ", elem,"/", max
	, " elapsed time ", "{:.2f}".format(t * elem), "s",sep = "", end = "\r"
	, flush=True)
elem += 1
print("ETA: ", "{:.2f}".format((max - elem) * t), "s [ "
	, int(elem * 100 / max), "%][", "=" * int(elem / max * len), ">"
	, " " * int(len - 1 - int(elem / max * len)), "] ", elem,"/", max
	, " elapsed time ", "{:.2f}".format(t * elem), "s",sep = "", end = "\r"
	, flush=True)
print("\n", ret, sep = "")