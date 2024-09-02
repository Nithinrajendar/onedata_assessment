from django.urls import path
from .views import list_meal, create_meal, update_meal

urlpatterns = [
    path('fooditems/', list_meal, name='list-food-items'),          # GET: List food items
    path('fooditems/create/', create_meal, name='create-food-item'), # POST: Create a food item
    path('fooditems/<int:id>/update/', update_meal, name='update-food-item'),  # PATCH: Update a food item
]
