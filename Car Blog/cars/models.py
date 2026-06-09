from django.db import models

# Create your models here.

class Car(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.URLField()
    year = models.TextField(max_length=4)
    model = models.CharField(max_length=30)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    milespergalon = models.IntegerField()
    horsepower = models.IntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.title