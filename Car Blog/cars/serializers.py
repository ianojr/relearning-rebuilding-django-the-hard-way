from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "title", "description", "image", "year",
                    "model", "starting_price", "milespergalon", "horsepower", "rating")
        
