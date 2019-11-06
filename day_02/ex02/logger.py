import time
from random import randint
from getpass import getuser

def log(func):
	def inner1(*args, **kwargs):
		passed = time.time()
		name = func.__name__
		ret = func(*args, **kwargs)
		name = name.replace('_', ' ').title()
		passed = time.time() - passed
		f.write("({})Running: {}\t [ exec-time = {:.3f} {}s ]\n".format(getuser(), name, passed * (1000 if passed < 1 else 1), "m" * (passed < 1)))
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
if __name__ == "__main__":
	f = open("machine.log", 'w+')
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)
	f.close()