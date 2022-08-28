from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('', views.home, name = 'home'),
    path('ingredients/',views.list_ingredients,name='all_ingredients'),
    path('search_ingredients', views.search_ingredient, name='search-ingredient')

]
