from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("HIIIII from HOME APP home")

def about(request):
    return HttpResponse("HIIIII from HOME APP about")

def contact(request):
    return HttpResponse("HIIIII from HOME APP contact")