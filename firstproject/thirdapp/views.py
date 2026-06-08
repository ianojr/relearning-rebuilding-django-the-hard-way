from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Function based view
def third_app(request):
    return HttpResponse ("This is a third Function Greeting")

# Class Based Views
class ThirdApp(View):
    def get(self, request):
        return HttpResponse("This is the third class greeting")
