import pandas as pd
# from FileLoader import FileLoader

def proportionBySport(data, year, sport, gender):
	data = data[(data["Year"] == year) & (data["Sex"] == 'F')]
	return data[data["Sport"] == sport].shape[0] / data.shape[0]

# loader = FileLoader()
# data = loader.load('../athlete_events.csv')
# print(proportionBySport(data, 2004, 'Tennis', 'F'))