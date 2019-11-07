import numpy as np

class NumPyCreator():
	def __init__(self):
		pass

	def from_list(self,lst):
		return np.array(lst)

	def from_tuple(self,tpl):
		return np.array(tpl)


	def from_shape(self,shape, value = 0):
		return np.full(shape, value)


	def random(self,shape):
		return np.random.random(shape)

	def identity(self,n):
		return np.eye(n)

truc = NumPyCreator()
a = (1, 2, 3)
b = truc.from_tuple(a)
print("type :", type(b) ,"and", b)