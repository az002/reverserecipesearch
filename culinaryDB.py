import pandas as pd
from playground.models import *
import re,os

BASE = 'C:/Users/azcyb/Documents/DB/rsearch/utils'

RECIPES = pd.read_csv(os.path.join(BASE,'01_Recipe_Details.csv'))
INGREDIENTS = pd.read_csv(os.path.join(BASE,'02_Ingredients.csv'))
COMPOUND_INGREDIENTS = pd.read_csv(os.path.join(BASE,'03_Compound_Ingredients.csv'))
RECIPE_INGREDIENT = pd.read_csv(os.path.join(BASE,'04_Recipe-Ingredients_Aliases.csv'))

def loadIngredients():
    #Aliased Ingredient Name,   Ingredient Synonyms,    Entity ID,  Category
    for ingredient in INGREDIENTS.iterrows():

        ingredient = ingredient[1]
        print(ingredient['Aliased Ingredient Name'])
        I = Ingredient(id = ingredient['Entity ID'], ingredient_name = ingredient['Aliased Ingredient Name'], category = ingredient['Category'])
        I.save()
        alias = IngredientAlias(name = ingredient['Aliased Ingredient Name'], parent = I)
        alias.save()

        for syn in ingredient['Ingredient Synonyms'].split('; '):
            print('\t' + syn)
            a = IngredientAlias(name = syn, parent = I)
            a.save()
        
    #Compound Ingredient Name,  Compound Ingredient Synonyms,   entity_id,  Contituent Ingredients, Category
    for index, ingredient in COMPOUND_INGREDIENTS.iterrows():
        print(ingredient['Compound Ingredient Name'])
        I = Ingredient(id = ingredient['entity_id'], ingredient_name = ingredient['Compound Ingredient Name'], category = ingredient['Category'])
        I.save()
        alias = IngredientAlias(name = ingredient['Compound Ingredient Name'])

        for syn in ingredient['Compound Ingredient Synonyms'].split('; '):
            print('\t' + syn)
            a = IngredientAlias(name = syn, parent = I)
            a.save()

def loadRecipes():
    #Recipe ID,Title,Source,Cuisine
    #Recipe ID,Original Ingredient Name,Aliased Ingredient Name,Entity ID
    #k = 0
    for index, recipe in RECIPES.iterrows():
        if len(recipe['Title']) > 100:
            continue
        print(recipe['Title'])
        ID = recipe['Recipe ID']

        #if(Recipe.objects.filter(id=ID).count()):
        #    continue

        ingredients = set(RECIPE_INGREDIENT.loc[RECIPE_INGREDIENT['Recipe ID'] == ID]['Entity ID'])
        R = Recipe(id=recipe['Recipe ID'], recipe_name=recipe['Title'], source = recipe['Source'], cuisine = recipe['Cuisine'], ingredient_count = len(ingredients))
        R.save()
        
        Q = Ingredient.objects.filter(id__in=ingredients)
        #print(len(Q))
        for i in Q:
            print('\t'+i.ingredient_name)
            R.ingredients.add(i)
    

