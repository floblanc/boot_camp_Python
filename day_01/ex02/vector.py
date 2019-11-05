class Vector:
	def __init__(self, arg):
		if (isinstance(arg, int)):
			self.value = list(range(arg))
		elif (isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(i, int) for i in arg)):
			self.value = list(range(arg[0], arg[1]))
		elif (isinstance(arg, list) and all(isinstance(elem, float) for elem in arg)):
			self.value = arg
		else:
			print("Error")
			exit()
		self.value = [float(i) for i in self.value]
		self.length = len(self.value)
	def __add__(self, plus):
		if isinstance(plus, Vector) and plus.length == self.length:
			return Vector([self.value[i] + plus.value[i] for i in range(self.length)])
		if isinstance(plus, int) or isinstance(plus, float):
			return Vector([i + plus for i in self.value])
		print("Error")
		exit()

	def __radd__(self, plus):
		if isinstance(plus, Vector) and plus.length == self.length:
			return Vector([self.value[i] + plus.value[i] for i in range(self.length)])
		if isinstance(plus, int) or isinstance(plus, float):
			return Vector([i + plus for i in self.value])
		print("Error")
		exit()

	def __sub__(self, plus):
		if isinstance(plus, Vector) and plus.length == self.length:
			return Vector([self.value[i] - plus.value[i] for i in range(self.length)])
		if isinstance(plus, int) or isinstance(plus, float):
			return Vector([i - plus for i in self.value])
		print("Error")
		exit()

	def __rsub__(self, plus):
		if isinstance(plus, Vector) and plus.length == self.length:
			return Vector([plus.value[i] - self.value[i] for i in range(self.length)])
		if isinstance(plus, int) or isinstance(plus, float):
			return Vector([plus - i for i in self.value])
		print("Error")
		exit()
	
	def __truediv__(self, plus):
		if isinstance(plus, Vector) and plus.length == self.length:
			try:
				return Vector([self.value[i] / plus.value[i] for i in range(self.length)])
			except ZeroDivisionError:
				print("div by zero!")
				exit()
		if (isinstance(plus, int) or isinstance(plus, float)) and plus != 0:
			try:
				return Vector([i / plus for i in self.value])
			except ZeroDivisionError:
				print("div by zero!")
				exit()
		print("Error")
		exit()

	def __rtruediv__(self, plus):
		if isinstance(plus, Vector) and plus.length == self.length:
			try:
				return Vector([plus.value[i] / self.value[i] for i in range(self.length)])
			except ZeroDivisionError:
				print("div by zero!")
				exit()
		if (isinstance(plus, int) or isinstance(plus, float)):
			try:
				return Vector([plus / i for i in self.value])
			except ZeroDivisionError:
				print("div by zero!")
				exit()
		print("Error")
		exit()

	def __mul__(self, plus):
		if isinstance(plus, Vector) and plus.length == self.length:
			return Vector([self.value[i] * plus.value[i] for i in range(self.length)])
		if isinstance(plus, int) or isinstance(plus, float):
			return Vector([i * plus for i in self.value])
		print("Error")
		exit()

	def __rmul__(self, plus):
		if isinstance(plus, Vector) and plus.length == self.length:
			return Vector([self.value[i] * plus.value[i] for i in range(self.length)])
		if isinstance(plus, int) or isinstance(plus, float):
			return Vector([i * plus for i in self.value])
		print("Error")
		exit()

	def __str__(self):
		return ("Value : {}\nLength : {}".format(self.value, self.length))

	def __repr__(self):
	 return
