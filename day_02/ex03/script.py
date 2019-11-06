import csvreader
from csv import CsvReader

if __name__ == "__main__":
	# with CsvReader('good.csv', header = True) as file:
	with csvreader.Loadjson('good.csv', header = True) as file:
		if file == None:
			print("File is corrupted")
			exit()
		data = file.getdata()
		header = file.getheader()
		print("data = ", data)
		print("header = ", header)
