class CsvReader():
	def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.sep = sep
		self.isheader = header
		self.skip_top = skip_top
		self.skip_bottom = -skip_bottom

	def getdata(self):
		contents = (self.file.read()).split("\n")
		if self.skip_bottom != 0:
			contents = contents[:self.skip_bottom]
		self.data = []
		for i in contents[self.skip_top + self.isheader:]:
			self.data += i.split(self.sep)
		return self.data

	def getheader(self):
		self.file.seek(0)
		if self.isheader == True:
			return self.file.readline()[:-1]
		else:
			return None


class Loadjson(CsvReader):
	"""docstring for Loadjson"""
	def __init__(self, name, sep=',', header=False, skip_top=0, skip_bottom=0):
		super(Loadjson, self).__init__(sep, header, skip_top, skip_bottom)
		self.name = name

	def __enter__(self):
		try :
			self.file = open(self.name, "r")
		except OSError:
			print("fail to open", self.name)
			exit()
		return self

	def __exit__(self, type, value, traceback):
		self.file.close()

