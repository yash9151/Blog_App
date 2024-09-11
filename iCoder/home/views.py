from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    messages.error(request, "Welcome to contact")
    # messages.error(request, "Welcome to contact")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"Please fill the form Correctly")
        else:
            contact = Contact(name = name, email = email, phone = phone, content = content)
            contact.save()
            messages.success(request,"Your message has been successfully sent...")

    return render(request, "home/contact.html")

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = []
    else:
        allPosts = Post.objects.filter(title__icontains=query)
    if allPosts.count() == 0:
        messages.error(request, "No search result found please refine your query")
    params = {"allPosts" : allPosts, "query":query}
    return render(request,"home/search.html", params)
