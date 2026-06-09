from django.urls import path
from .views import CarListView, DetailCarView


urlpatterns = [
    path("", CarListView.as_view(), name="car_list"),
    path("<int:pk>", DetailCarView.as_view(), name="detailed_list"),
]

