import time
import sys

def ft_progress(listy):
	maxi = max(listy)
	start_t = time.time()
	len = 30
	for i in listy:
		passed = time.time() - start_t
		if i == 0:
			va = 0.0
		else:
			va = float((maxi / i) * passed)
		print("ETA: {:.2f}s [{}%][{}{}{}] {}/{} | elapsed time {:.2f}s".format(va
		, int(i * 100 / maxi), "=" * int(i / maxi * len), ">" * (i != maxi)
		, " " * int(len - 1 - int((i / maxi) * len)), i + 1, maxi + 1, passed), end="\r"
		, flush=True)
		if i == maxi:
			print("")
		yield i
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print(ret)