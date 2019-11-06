import time
from random import randint
import getpass

def log(func):
		def inner1(*args, **kwargs): 
			name = func.__name__
			name = name.replace("_", " ").title()
			past = time.time()
			ret = func(*args, **kwargs)
			res = time.time() - past
			string = "({})Running: {}\t [ exec-time = {:.3f} {}s ]\n".format(getpass.getuser(), name, res * (1000 if res < 1 else 1), "m" * (res < 1))
			f.write(string)
			return ret
		return inner1

class CoffeeMachine():
	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")
