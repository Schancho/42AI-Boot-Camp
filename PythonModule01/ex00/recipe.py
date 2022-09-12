# You will have to make a class Book and a class Recipe. The classes Book and Recipe
# will be written in book.py and recipe.py respectively.
# Let’s describe the Recipe class. It has some attributes:
# • name (str): name of the recipe,
# • cooking_lvl (int): range from 1 to 5,
# • cooking_time (int): in minutes (no negative numbers),
# • ingredients (list): list of all ingredients each represented by a string,
# • description (str): description of the recipe,
# • recipe_type (str): can be "starter", "lunch" or "dessert".
# You have to initialize the object Recipe and check all its values, only the description
# can be empty. In case of input errors, you should print what they are and exit properly.
# You will have to implement the built-in method __str__. It’s the method called when
# the following code is executed:
# 3
# Python & ML - Module 01 Basic 2
# tourte = Recipe(...)
# to_print = str(tourte)
# print(to_print)
# It is implemented this way:
# def __str__(self):
# """Return the string to print with the recipe info"""
# txt = ""
# """Your code here"""
# return txt
# The Book class also has some attributes:
# • name (str): name of the book,
# • last_update (datetime): the date of the last update,
# • creation_date (datetime): the creation date,
# • recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert".
# You will have to implement some methods in Book class:
# def get_recipe_by_name(self, name):
# """Prints a recipe with the name \texttt{name} and returns the instance"""
# #... Your code here ...
# def get_recipes_by_types(self, recipe_type):
# """Get all recipe names for a given recipe_type """
# #... Your code here ...
# def add_recipe(self, recipe):
# """Add a recipe to the book and update last_update"""
# #... Your code here ...
# You have to handle the error if the argument passed in add_recipe is not a Recipe.
# Finally, you will provide a test.py file to test your classes and prove that they are
# working properly. You can import all the classes into your test.py file by adding these
# lines at the top of the test.py file:
# from book import Book
# from recipe import Recipe
# # ... Your tests ...

class Recipe:
    def __init__(self, name=None, cooking_lvl=None, cooking_time=None, ingredients=None, description='', recipe_type=None):
        for i in [name, cooking_lvl, cooking_time, ingredients, recipe_type]:
            if i == None:
                print("Error: missing argument")
                exit(1) 
        self.name = str(name)
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = list(ingredients)
        self.description = str(description)
        self.recipe_type = str(recipe_type)
        if self.cooking_lvl < 1 or self.cooking_lvl > 5:
            print("cooking level must be between 1 and 5")
            exit(1)
        if self.cooking_time < 0:
            print("cooking time must be positive")
            exit(1)
        if self.recipe_type != "starter" and self.recipe_type != "lunch" and self.recipe_type != "dessert":
            print("recipe type must be starter, lunch or dessert")
            exit(1)
        
    def __str__(self):
        text =  "Recipe name:   " + self.name + "\n"
        text += "Cooking level: " + str(self.cooking_lvl) + "\n"
        text += "Cooking time:  " + str(self.cooking_time) + "\n"
        text += "Ingredients:   " 
        for i in self.ingredients:
            text += i + ", "
        text += "\nDescription:   " + self.description + "\n"
        text += "Recipe type:   " + self.recipe_type
        return text

rec = Recipe("test", 1, 10, ["test", "test2"], "test", "starter")
to_print = str(rec)
print(to_print)
# print(rec)

    
