# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:52:00 2024

@author: Amitr
"""

class Recipe:
    def __init__(self, name, ingredients, cuisine):
        self.name = name
        self.ingredients = ingredients  # List of Ingredient objects
        self.cuisine = cuisine

    def __repr__(self):
        return f"Recipe: {self.name} ({self.cuisine})"

    def get_ingredients(self):
        return [(ingredient.name, ingredient.quantity, ingredient.unit) for ingredient in self.ingredients]

# Example usage
# recipe = Recipe('Spaghetti Carbonara', [Ingredient('spaghetti', 250, 'g')], 'Italian')
