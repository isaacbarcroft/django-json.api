from django.urls import path, include
from . import views
from rest_framework import routers

# app_name= 'recipes'

router = routers.DefaultRouter()
router.register(r'recipes', views.RestaurantViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('<name>/', views.RecipeListAPIView.as_view(),name='recipe_list'),

]