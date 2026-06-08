from django.urls import path
from .views import ListTodo, DetailedTodo

urlpatterns = [
    path("", ListTodo.as_view(), name="todo_list"),
    path("<int:pk>", DetailedTodo.as_view(), name="detailed_todo"),
]
