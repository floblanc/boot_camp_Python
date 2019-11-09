import pandas as pd
# from FileLoader import FileLoader

def howManyMedals(data, name):
	data = data.loc[data["Name"] == name][["Year", "Medal"]]
	res = {}
	for y in data["Year"].unique():
		tmp = {'G' : data[(data["Year"] == y) & (data["Medal"] == "Gold")]["Medal"].size}
		tmp["S"] = data[(data["Year"] == y) & (data["Medal"] == "Silver")]["Medal"].size
		tmp["B"] = data[(data["Year"] == y) & (data["Medal"] == "Bronze")]["Medal"].size
		print (tmp)
	return res

# loader = FileLoader()
# data = loader.load('../athlete_events.csv')
# print(howManyMedals(data,'Kjetil Andr Aamodt'))