from django.contrib import admin
from .models import Car

# Register your models here.


class AdminCars(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image", "year",
                    "model", "starting_price", "milespergalon", "horsepower", "rating")

admin.site.register(Car, AdminCars)