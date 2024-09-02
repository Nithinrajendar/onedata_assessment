from rest_framework import serializers
from .models import MealReceipe

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealReceipe
        fields = ['id', 'name', 'description', 'ingredients', 'method', 'category']

    def validate_name(self, value):
        if MealReceipe.objects.filter(name=value).exists():
            raise serializers.ValidationError("A food item with this name already exists.")
        return value
