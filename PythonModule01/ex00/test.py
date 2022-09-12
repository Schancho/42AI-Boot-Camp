from book import Book
from recipe import Recipe
from time import time

tourte = Recipe("tourte", 5, 5, ["Milk", "eggs"], "cake", "lunch")
to_print = str(tourte)
print(to_print)

cookbook = Book("cook", time(), time(), tourte)
print("===New recipe in Book===")
cookbook.add_recipe(tourte)
cookbook.get_recipe_by_name(tourte)
print("===Get recipes by types===")
cookbook.get_recipes_by_types("lunch")