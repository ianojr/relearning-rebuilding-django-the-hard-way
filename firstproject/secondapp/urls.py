from django.urls import path
from . import views


urlpatterns = [
    path("kenya", views.hello_kenya),
    path("tanzania", views.HelloTanzania.as_view())
]
