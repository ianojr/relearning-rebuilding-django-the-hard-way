from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Function Based Views
def hello_kenya(request):
    return HttpResponse("Hello From Kenya!")


# Class Based Views
class HelloTanzania(View):
    def HelloTanzania(self, request):
        return HttpResponse("Habari Kutoka Tanzania!")