from home import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
]
