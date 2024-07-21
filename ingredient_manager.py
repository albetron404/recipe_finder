# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:59:23 2024

@author: Amitr
"""
from ingredient import Ingredient
from datetime import datetime

class IngredientManager:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, name, quantity, unit, expiry_date=None):
        try:
            ingredient = Ingredient(name, quantity, unit, expiry_date)
            self.ingredients.append(ingredient)
            print(f"Added: {ingredient}")
        except ValueError as e:
            print(e)

    def remove_ingredient(self, name):
        self.ingredients = [ingredient for ingredient in self.ingredients if ingredient.name != name]
        print(f"Removed: {name}")

    def update_quantity(self, name, quantity):
        for ingredient in self.ingredients:
            if ingredient.name == name:
                ingredient.quantity = quantity
                print(f"Updated quantity for {name}: {quantity} {ingredient.unit}")
                return
        print(f"Ingredient {name} not found")

    def update_expiry_date(self, name, expiry_date):
        for ingredient in self.ingredients:
            if ingredient.name == name:
                ingredient.expiry_date = expiry_date
                print(f"Updated expiry date for {name}: {expiry_date}")
                return
        print(f"Ingredient {name} not found")

    def list_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)

# Example usage
if __name__ == '__main__':
    manager = IngredientManager()
    manager.add_ingredient('tomato', 200, 'g', datetime(2024, 7, 21))
    manager.add_ingredient('milk', 1, 'l', datetime(2024, 8, 1))
    manager.list_ingredients()
    manager.update_quantity('tomato', 300)
    manager.update_expiry_date('milk', datetime(2024, 9, 1))
    manager.remove_ingredient('tomato')
    manager.list_ingredients()
