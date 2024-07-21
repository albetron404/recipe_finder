# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:52:08 2024

@author: Amitr
"""

from ingredient import Ingredient
from recipe import Recipe
from datetime import datetime

class RecipeFinder:
    def __init__(self, available_ingredients, recipes):
        self.available_ingredients = available_ingredients
        self.recipes = recipes

    def check_ingredient_availability(self, required_ingredient):
        for ingredient in self.available_ingredients:
            if (ingredient.name == required_ingredient.name and 
                ingredient.quantity >= required_ingredient.quantity and 
                ingredient.unit == required_ingredient.unit and 
                not ingredient.is_expired()):
                return True
        return False

    def find_recipes(self):
        matching_recipes = []
        for recipe in self.recipes:
            if all(self.check_ingredient_availability(ingredient) for ingredient in recipe.ingredients):
                matching_recipes.append(recipe)
        return matching_recipes

# Example usage
# finder = RecipeFinder(available_ingredients, all_recipes)
# matching_recipes = finder.find_recipes()
# print(matching_recipes)
