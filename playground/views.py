from django.shortcuts import render
from .models import Recipe,Ingredient
import numpy as np
# Create your views here.

QUERY_BASE = 'select r.id, r.recipe_name, r_count.cnt, r_count_all.cnt_all from playground_recipe as r \
                inner join ( \
                    select recipe_id, count(*) cnt \
                    from playground_recipe_ingredients \
                    where ingredient_id in {} \
                    group by recipe_id \
                ) as r_count \
                    on r.id = r_count.recipe_id \
                inner join ( \
                    select recipe_id, count(*) cnt_all \
                    from playground_recipe_ingredients \
                    group by recipe_id \
                ) as r_count_all \
                    on r.id = r_count_all.recipe_id \
                where r_count.cnt = r_count_all.cnt_all;'

def list_ingredients(request):
    ingredients = Ingredient.objects.all().order_by('ingredient_name')
    return render(request, 'ingredients.html', {'ingredients':ingredients})

def search_ingredient(request):
    def clean(string):
        return string.lstrip().title()
    if request.method == "POST":
        CLEAN = np.vectorize(clean)
        if request.POST['SEARCHED']:
            query = list(CLEAN(np.array(request.POST['SEARCHED'].split(','))))
            #ingredients_list = Ingredient.objects.filter(ingredient_name__in=query).values_list('id', flat=True)

            q_dict = {}
            ingredients_list = list()
            for q in query:
                FIND = Ingredient.objects.filter(ingredient_name=str(q)).values_list('id', flat=True)
                if FIND:
                    q_dict[q] = 'FOUND'
                    ingredients_list.append(FIND[0])
                else:
                    q_dict[q] = 'NOT FOUND'
            if ingredients_list:
                ingredients_list.append(' ')
                I_LIST = str(tuple(ingredients_list))
                recipe_list = list(Recipe.objects.raw(QUERY_BASE.format(I_LIST)))
                return render(request, 'search.html', {'query':query, 'q_dict':q_dict, 'recipe_list':recipe_list})
            return render(request, 'search.html', {'query':query, 'q_dict':q_dict, 'recipe_list':[]})
        else:
            return render(request, 'search.html', {'query':False})
    else:
        return render(request, 'search.html', {'query':False})

def home(request):
    num_recipes = Recipe.objects.all().count()
    num_ingredients = Ingredient.objects.all().count()
    return render(request, 'home.html', {'num_recipes' : num_recipes, 'num_ingredients' : num_ingredients})