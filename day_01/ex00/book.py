from datetime import date
from recipe import Recipe

class Book:
	def __init__(self, name):
		try:
			if not isinstance(name, str):
				raise TypeError("name")
			if name == "":
				raise ValueError("name")
			self.name = name
			self.last_update = date.today()
			self.creation_date = self.last_update
			self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}
		except TypeError as e:
			print("Type error with", e)
			exit()
		except ValueError as e:
			print("Value error with", e)
			exit()
	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for r_type in self.recipes_list:
			for elem in self.recipes_list[r_type]:
				if name == elem.name:
					print (elem)
					return elem
				else:
					print("Bad name")
					exit()
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		if recipe_type not in self.recipes_list:
			print("This is not a recipe type")
			exit()
		
		for i in self.recipes_list[recipe_type]:
			print(i.name)
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if isinstance(recipe, Recipe):
			self.recipes_list[recipe.recipe_type].append(recipe)
			self.last_update = date.today()
		else:
			print("This is not a recipe")
			exit()