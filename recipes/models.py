from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255, null=True)
    ingredients = models.TextField(null=True)
    instructions = models.TextField(null=True)


# Recipe.objects.filter(json__isnull=True)