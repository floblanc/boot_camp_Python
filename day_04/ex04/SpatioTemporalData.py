import pandas as pd
# from FileLoader import FileLoader

class SpatioTemporalData():
	def __init__(self, data):
		self.data = data

	def when(self, location):
		return list(self.data.loc[self.data["City"] == location]["Year"].unique())

	def where(self, date):
		return list(self.data.loc[self.data["Year"] == date]["City"].unique())


# loader = FileLoader()
# data = loader.load('../athlete_events.csv')
# sp = SpatioTemporalData(data)
# print(sp.when('Athina'))
# print(sp.where(2016))