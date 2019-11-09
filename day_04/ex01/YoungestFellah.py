import pandas as pd
# from FileLoader import FileLoader

def youngestFellah(data, year):
	F = data[(data["Sex"] == 'F') & (data["Year"] == year)]
	M = data[(data["Sex"] == 'M') & (data["Year"] == year)]
	return {'f' : F["Age"].min(), 'm' : M["Age"].min()}
# loader = FileLoader()
# print(youngestFellah(loader.load('../athlete_events.csv'), 2004))