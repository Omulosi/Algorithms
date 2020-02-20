#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    whole_batches = []
    try:
        for key in recipe:
            whole_batches.append(ingredients[key] // recipe[key])
    except KeyError:
        # recipe item not in ingredients
        whole_batches.append(0)
    return min(whole_batches)



if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
