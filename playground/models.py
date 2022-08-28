from django.db import models
from django.urls import reverse

# Create your models here.

class Ingredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    ingredient_name = models.CharField(max_length = 100, blank = False)
    category = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        return self.ingredient_name
    
    class Meta:
        indexes = [models.Index(fields=['ingredient_name'])]

class IngredientAlias(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    parent = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = 'aliases')
    def __str__(self):
        return self.alias

class Recipe(models.Model):
    id = models.BigAutoField(primary_key = True)
    recipe_name = models.CharField(max_length = 100, blank = False)
    ingredient_count = models.PositiveSmallIntegerField(blank=False)
    source = models.CharField(max_length = 100, blank = False)
    cuisine = models.CharField(max_length = 100, blank = False)
    ingredients = models.ManyToManyField(Ingredient)
    
    def __str__(self):
        return self.recipe_name
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    class Meta:
        indexes = [
            models.Index(fields=['recipe_name','ingredient_count']),
            models.Index(fields=['ingredient_count']),
            models.Index(fields=['recipe_name'])
        ]
        
