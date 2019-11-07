import numpy as np

class ColorFilter():
	def __init__(self):
		pass

	def invert(self, array):
		return 1 - array
	
	def to_blue(self, array):
		new = np.zeros(array.shape)
		new[:, :, 2:] = array[:, :, 2:]
		return new

	def to_green(self, array):
		return array * (0, 1, 0)

	def to_red(self,array):
		return array - (self.to_green(array) + self.to_blue(array))

	def celluloid(self, array):
		pass


a = np.random.random((5,5,3))
print(a)
ap = ColorFilter()
print(ap.to_red(a))