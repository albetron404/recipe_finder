# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:43:43 2024

@author: Amitr
"""
from datetime import datetime
from recipe_finder import RecipeFinder
from recipes import ALL_RECIPES
from ingredient_manager import IngredientManager

def main():
    # Initialize IngredientManager and add initial ingredients
    ingredient_manager = IngredientManager()
    ingredient_manager.add_ingredient('spaghetti', 500, 'g', datetime(2024, 8, 21))
    ingredient_manager.add_ingredient('eggs', 10, 'units', datetime(2024, 7, 25))
    ingredient_manager.add_ingredient('parmesan cheese', 100, 'g', datetime(2024, 7, 30))
    ingredient_manager.add_ingredient('pancetta', 200, 'g', datetime(2024, 8, 1))
    ingredient_manager.add_ingredient('black pepper', 20, 'g', datetime(2025, 1, 1))

    # List current ingredients
    print("\nCurrent Ingredients:")
    ingredient_manager.list_ingredients()

    # Perform some operations
    ingredient_manager.update_quantity('eggs', 12)
    ingredient_manager.update_expiry_date('black pepper', datetime(2025, 2, 1))
    ingredient_manager.remove_ingredient('pancetta')

    # List updated ingredients
    print("\nUpdated Ingredients:")
    ingredient_manager.list_ingredients()

    # Create RecipeFinder instance
    recipe_finder = RecipeFinder(ingredient_manager.ingredients, ALL_RECIPES)

    # Find and print matching recipes
    matching_recipes = recipe_finder.find_recipes()
    if matching_recipes:
        print("\nMatching Recipes:")
        for recipe in matching_recipes:
            print(recipe)
    else:
        print("\nNo matching recipes found with available ingredients.")

if __name__ == '__main__':
    main()
