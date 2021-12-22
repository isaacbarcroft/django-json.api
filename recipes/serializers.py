from rest_framework_json_api import serializers
from .models import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'ingredients', 'instructions')