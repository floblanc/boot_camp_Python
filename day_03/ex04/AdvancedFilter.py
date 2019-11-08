import numpy as np
from ScrapBooker import ScrapBooker

class AdvancedFilter():
	def __init__(self):
		pass

	def mean_blur(self, array):
		new = []
		maxi = array.shape
		# print(“maxi =“, maxi)
		for i in range (maxi[0]):
			i = i - 1
			for j in range (maxi[1]):
				j = j - 1
				s = np.sum((array[(i if i >= 0 else 0):(i + 3 if (i + 3) < maxi[0] else maxi[0] - 1),
										(j if j >= 0 else 0):(j + 3 if (j + 3) < maxi[1] else maxi[1] - 1)]), 1)
				s = sum(s) / (s.shape[0] * s.shape[1])
				new = np.append(new, s)
		new.shape = array.shape
		return new


a = np.random.random((5,5,3))
print(a)
ap = AdvancedFilter()
b = [[[1,.5,.1],[1,.5,.1],[1,.5,.1]],[[1,.5,.1],[1,.5,.1],[1,.5,.1]],[[1,.5,.1],[1,.5,.1],[1,.5,.1]]]
b = np.array(b)
print("-|------------------------------------------------------------------------------|")
print (a)
print("|------------------------------------------------------------------------------|")
print(ap.mean_blur(a))