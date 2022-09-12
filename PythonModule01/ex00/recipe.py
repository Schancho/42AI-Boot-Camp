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

    
