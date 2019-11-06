import time
import sys
import ai42

listy = range(1000)
ret = 0
for elem in ai42.progressbar.ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print(ret)