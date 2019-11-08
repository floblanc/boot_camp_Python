import numpy as np

class ScrapBooker():
	def __init__(self):
		pass

	def crop(self,array, dimensions, position = (0,0)):
		try:
			tmp = array[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]]
		except Exception:
			print("Error")
			exit()
		return tmp

	def thin(self, array, n, axis = None):
		return np.delete(array, np.s_[n::n], axis)

	def juxtapose(self, array, n, axis = None):
		return np.repeat(array, n, axis)

	def  mosaic(self, array, dimensions) :
		return np.tile(array, dimensions)

a = np.random.random((5,5,3))
print(a)
ap = ScrapBooker()
print ("/////////\n", ap.crop(a, (3,3), (2,1)))

c = np.array(['A','B','C','D','E','F','G','H','I','J','K','L'])
# print (c)
# print(ap.thin(c,3))
# print("-----------------------------------------")
# print(ap.thin(a,3,1))
# print("-----------------------------------------")
# print(ap.juxtapose(a,2))
# print("-----------------------------------------")
# print(ap.juxtapose(a,2,1))
# print("-----------------------------------------")
# print(ap.mosaic(a, (2,2)))
# print()