cookbook = {"sandwich" : {"ingedients" : ("ham", "bread", "cheese", "tomatoes")
, "meal" : "lunch", "prep_time" : 10},
"cake" : {"ingedients" : ("flour", "sugar", "eggs"), "meal" : "dessert"
, "prep_time" : 60},
"salad" : {"ingedients" : ("avocado", "arugula", "tomatoes", "spinach")
, "meal" : "lunch", "prep_time" : 15}}

#1
# for x in cookbook:
#   print(x)

# for x in cookbook.values():
#   print(x)

# for x, y in cookbook.items():
# 	print(x, y)

#2
def print_recipe(name):
	if (name in cookbook):
		print(name, "recipe :", cookbook[name])
	else:
		print("This recipe does'nt exist")

#3
def delete_recipe(name):
	if (name in cookbook):
		cookbook.pop(name)
	else:
		print("This recipe does'nt exist")

#4
def add_recipe(name, ingredients, meal, time):
	cookbook[name] = {"ingredients" : ingredients, "meal" : meal
	, "prep_time" : time}

#5
def print_all_names():
	print("List of recipes : ", end = "")
	print(*cookbook, sep = ", ")

6#
answer = False
n = input("Please select an option by typing the corresponding number:\n")
while answer == False:
	answer = True
	if n == "1":
		name = input("Please enter the recipe's name to add:\n")
		ingr = input("Please enter the recipe's ingredients list:\n")
		meal = input("Please enter the recipe's type of meal:\n")
		time = input("Please enter the recipe's preparation time(in min):\n")
		add_recipe(name, ingr, meal, time)
	elif n == "2":
		name = input("Please enter the recipe's name to delete:\n")
		delete_recipe(name)
	elif n == "3":
		name = input("Please enter the recipe's name to get its details:\n")
		print_recipe(name)
	elif n == "4":
		print_all_names()
	elif n == "5":
		print("Cookbook closed")
		exit()
	else:
		answer = False
		print("This option does not exist, please type the ", end = "")
		n = input("corresponding number.\nTo exit, enter 5.\n")