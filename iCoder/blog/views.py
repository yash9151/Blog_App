from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("HIIIII from blogHome")

def blogPost(request, slug):
    return HttpResponse(f"HIIIII from blogPost: {slug}")
