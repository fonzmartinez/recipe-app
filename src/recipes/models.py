from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_id= models.AutoField(primary_key=True)
    recipe_name= models.CharField(max_length=120)
    ingredients= models.TextField()
    cooking_time= models.PositiveIntegerField()

    def __str__(self):
        return str(self.recipe_name)
