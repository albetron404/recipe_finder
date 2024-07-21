# Recipe Finder

This project is a Recipe Finder application that suggests recipes based on the ingredients you have at home. It considers ingredient availability and expiry dates.

## Features

- Add recipes with ingredients, quantities, and units.
- Check for ingredient availability and expiry.
- Suggest matching recipes based on available ingredients.
- Extensible for adding more recipes and ingredients.

## File Structure

recipe_finder/
│
├── main.py
├── ingredient.py
├── recipe.py
├── recipe_finder.py
├── recipes.py
└── README.md

## Getting Started

1. Clone the repository.
2. Navigate to the `recipe_finder` directory.
3. Run `main.py` to see the matching recipes based on the available ingredients.

```bash
python main.py
Adding More Recipes
To add more recipes, edit the recipes.py file and extend the lists for each cuisine.
Adding More Ingredients
To add more ingredients, edit the recipes.py file and extend the available_ingredients list.
License
This project is licensed under the MIT License.
