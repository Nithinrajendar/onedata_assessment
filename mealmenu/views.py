from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MealReceipe
from .serializers import MealSerializer 


# Create your views here.

@api_view(['GET'])
def list_meal(request):
    category = request.query_params.get('category')
    queryset = MealReceipe.objects.all() if not category else MealReceipe.objects.filter(category=category)
    
    serializer = MealSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_meal(request):
    serializer = MealSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PATCH'])
def update_meal(request, id=None):
    try:
        food_item = MealReceipe.objects.get(id=id)
    except MealReceipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MealSerializer(food_item, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
