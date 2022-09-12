import time
from recipe import Recipe
from datetime import datetime

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        recipes_list = {
            "lunch": 0,
            "starter": 0,
            "dessert": 0
        }
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        try:
            if self.recipes_list['lunch'] == name:
                print(self.recipes_list['lunch'])
                return self.recipes_list['lunch']
        except:
            pass
        try:
            if self.recipes_list['starter'] == name:
                print(self.recipes_list['starter'])
                return self.recipes_list['starter']
        except:
            pass
        try:
            if self.recipes_list['dessert'] == name:
                print(self.recipes_list['dessert'])
                return self.recipes_list['dessert']
        except:
            pass
        print("No recipe found with this name")
        return None

    def get_recipes_by_types(self, recipe_type):
        try:
            if self.recipes_list[recipe_type] != 0:
                print(self.recipes_list[recipe_type])
                return self.recipes_list[recipe_type]
        except:
            pass
        print("No recipe found with this type")
        return None

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type] = recipe
            self.last_update = datetime.now()
            print("Recipe added")
        else:
            print("This is not a recipe")

