from book import Book
from recipe import Recipe

# tourte = Recipe("Burger", 5, 30, ["steak","bread"], "BK", "lunch")
# # to_print = str(tourte)
# # print(to_print)

# livre = Book("l'ortolan de Maite")
# livre.add_recipe(tourte)
# livre.get_recipe_by_name("Burger")
tourte = Recipe("tourte", 2, 12, ["tourte"], "tourte", "lunch")
steak = Recipe("steak", 2, 12, ["steak"], "steak", "starter")
glace = Recipe("glace", 2, 12, ["glace"], "glace", "dessert")
glaces = Recipe("glaces", 2, 12, ["glace"], "glace", "dessert")
glacess = Recipe("glacess", 2, 12, ["glace"], "glace", "dessert")
maman = Book("Bonne Maman")
maman.add_recipe(glace)
maman.add_recipe(glaces)
maman.add_recipe(glacess)
maman.get_recipe_by_name("glace")
maman.get_recipes_by_types("dessert")