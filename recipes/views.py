from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import viewsets, generics 


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer



class RecipeListAPIView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Recipe.objects.filter(name=name)