import numpy as np
import matplotlib.pyplot as plt
import matplotblib.image as mpimg

class ImageProcessor():
	def __init__(self):
		pass

	def load(self, path):
		try:
			img = np.array(mpimg.imread(path))
		except Exception:
			print("Invalid path")
			exit()
		print("Loading image of dimensions {} x {}".format(img.shape[1], img.shape[0]))
		return img

	def display(self, array):
		try:
			plt.imshow(array)
			plt.show()
		except Exception:
			print("Invalid array")
			exit()
