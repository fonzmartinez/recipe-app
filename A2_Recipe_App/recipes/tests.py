from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(recipe_id='1', recipe_name='Pizza',
        ingredients='dough, cheese, pepperoni', cooking_time='5')

    def test_recipe_name(self):
        recipe = Recipe.objects.get(recipe_id=1)
        field_label = recipe._meta.get_field('recipe_name').verbose_name
        self.assertEqual(field_label, 'recipe name')

    def test_recipe_name_max_length(self):
          recipe = Recipe.objects.get(recipe_id=1)
          max_length = recipe._meta.get_field('recipe_name').max_length
          self.assertEqual(max_length, 120)

