class Recipe:
	def __init__(self, name, lvl, time, ingredients, description, r_type):
		try:
			if not isinstance(name, str):
				raise TypeError("name")
			if name == "":
				raise ValueError("name")
			if not isinstance(lvl, int):
				raise TypeError("cooking_lvl")
			if lvl < 1 or lvl > 5:
				raise ValueError("cooking_lvl")
			if not isinstance(time, int):
				raise TypeError("cooking_time")
			if time < 0:
				raise ValueError("cooking_time")
			if not all(isinstance(elem, str) for elem in ingredients):
				raise TypeError("ingredients")
			if not all(len(elem) != 0 for elem in ingredients):
				raise ValueError("ingredients")
			if not isinstance(description, str):
				raise TypeError("description")
			if description == "":
				raise ValueError("descritption")
			if not isinstance(r_type, str):
				raise TypeError("recipe_type")
			if (r_type != "starter" and r_type != "lunch"
				and r_type != "dessert"):
				raise ValueError("recipe_type")
			self.name = name
			self.cooking_lvl = lvl
			self.cooking_time = time
			self.ingredients = ingredients
			self.description = description
			self.recipe_type = r_type
		except TypeError as e:
			print("Type error with", e)
			exit()
		except ValueError as e:
			print("Value error with", e)
			exit()
	
	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = "Recipe's name : {}\nDifficulty : {}/5\nCooking time {} min\nIngredients : {}\nDescription : {}\nType : {}".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
		return txt
		"""Your code goes here"""