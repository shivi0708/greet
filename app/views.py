from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hey there! Enter /your_name")

def greet(request,name):
    return render(request, "app/greet.html" , {"name" : name.capitalize()}) 
