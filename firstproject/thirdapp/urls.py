from django.urls import path
from . import views


urlpatterns = [
    path("function", views.third_app),
    path("class", views.ThirdApp.as_view()),
]
