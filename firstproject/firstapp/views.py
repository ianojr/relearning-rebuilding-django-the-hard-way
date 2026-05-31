from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# Functions based views
def hello_world(request):
    return HttpResponse("Hello World!")


#Class based Views
class HelloKenya(View):
    def get(self, request):
        return HttpResponse("Hello from kenya!")