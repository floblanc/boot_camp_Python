import pandas as pd

class FileLoader():
	def __init__(self):
		pass

	def load(self, path):
		try:
			data = pd.read_csv(path)
			print("Loading dataset of dimensions {} x {}".format(data.shape[0], data.shape[1]))
			return data
		except Exception:
			print ("Error")
			exit()

	def display(self, df, n):
		print(df[:n])