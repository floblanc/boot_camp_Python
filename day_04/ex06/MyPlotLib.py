import pandas as ps
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from FileLoader import FileLoader

class MyPlotLib():
	def __init__(self):
		pass

	def histogram(self, data, features):
		data.hist(list(features))
		plt.show()

	def density(self, data, features):
		plot(density(data[features[0]]))
		plt.show()


loader = FileLoader()
data = loader.load('../athlete_events.csv')
mp = MyPlotLib()
# mp.histogram(data,("Height", "Weight"))
mp.density(data,("Height", "Weight"))
