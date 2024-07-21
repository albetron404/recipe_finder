# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:52:17 2024

@author: Amitr
"""

from ingredient import Ingredient
from recipe import Recipe
from datetime import datetime

# Define recipes here
italian_recipes = [
    Recipe('Spaghetti Carbonara', [
        Ingredient('spaghetti', 250, 'g'), 
        Ingredient('eggs', 4, 'units'), 
        Ingredient('parmesan cheese', 50, 'g'), 
        Ingredient('pancetta', 100, 'g'), 
        Ingredient('black pepper', 5, 'g')
    ], 'Italian'),
    # Add more recipes...
]

indian_recipes = [
    Recipe('Butter Chicken', [
        Ingredient('chicken', 500, 'g'), 
        Ingredient('butter', 50, 'g'), 
        Ingredient('cream', 100, 'ml'), 
        Ingredient('tomatoes', 200, 'g'), 
        Ingredient('garam masala', 10, 'g')
    ], 'Indian'),
    # Add more recipes...
]

mexican_recipes = [
    Recipe('Tacos', [
        Ingredient('tortillas', 200, 'g'), 
        Ingredient('ground beef', 300, 'g'), 
        Ingredient('onions', 100, 'g'), 
        Ingredient('tomatoes', 100, 'g'), 
        Ingredient('lettuce', 50, 'g'), 
        Ingredient('cheese', 100, 'g')
    ], 'Mexican'),
    # Add more recipes...
]

chinese_recipes = [
    Recipe('Kung Pao Chicken', [
        Ingredient('chicken', 300, 'g'), 
        Ingredient('peanuts', 50, 'g'), 
        Ingredient('bell peppers', 100, 'g'), 
        Ingredient('soy sauce', 30, 'ml'), 
        Ingredient('garlic', 10, 'g'), 
        Ingredient('ginger', 10, 'g')
    ], 'Chinese'),
    # Add more recipes...
]

american_recipes = [
    Recipe('Burger', [
        Ingredient('ground beef', 200, 'g'), 
        Ingredient('burger buns', 100, 'g'), 
        Ingredient('cheese', 50, 'g'), 
        Ingredient('lettuce', 20, 'g'), 
        Ingredient('tomatoes', 50, 'g'), 
        Ingredient('onions', 30, 'g')
    ], 'American'),
    # Add more recipes...
]

# Combine all recipes
all_recipes = italian_recipes + indian_recipes + mexican_recipes + chinese_recipes + american_recipes

# Example available ingredients
available_ingredients = [
    Ingredient('spaghetti', 500, 'g', datetime(2024, 8, 21)),
    Ingredient('eggs', 10, 'units', datetime(2024, 7, 25)),
    Ingredient('parmesan cheese', 100, 'g', datetime(2024, 7, 30)),
    Ingredient('pancetta', 200, 'g', datetime(2024, 8, 1)),
    Ingredient('black pepper', 20, 'g', datetime(2025, 1, 1)),
    Ingredient('ground beef', 500, 'g', datetime(2024, 7, 25)),
    Ingredient('lettuce', 200, 'g', datetime(2024, 7, 22)),
    Ingredient('cheese', 300, 'g', datetime(2024, 8, 1)),
    Ingredient('chicken', 1000, 'g', datetime(2024, 7, 28)),
    Ingredient('onions', 500, 'g', datetime(2024, 8, 5)),
    Ingredient('tomatoes', 500, 'g', datetime(2024, 7, 28)),
    Ingredient('garlic', 100, 'g', datetime(2024, 10, 1)),
    Ingredient('ginger', 100, 'g', datetime(2024, 10, 1)),
    Ingredient('butter', 200, 'g', datetime(2024, 9, 1)),
    Ingredient('cream', 200, 'ml', datetime(2024, 8, 10)),
    Ingredient('tortillas', 300, 'g', datetime(2024, 8, 1)),
    Ingredient('soy sauce', 200, 'ml', datetime(2025, 1, 1)),
    Ingredient('peanuts', 100, 'g', datetime(2025, 1, 1)),
    Ingredient('bell peppers', 200, 'g', datetime(2024, 7, 25)),
    Ingredient('burger buns', 200, 'g', datetime(2024, 7, 25)),
]

# Save as a global variable to be used by main.py
ALL_RECIPES = all_recipes
AVAILABLE_INGREDIENTS = available_ingredients
