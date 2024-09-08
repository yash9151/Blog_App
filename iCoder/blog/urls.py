from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.blogHome, name="blogHome"),
    path('<str:slug>/', views.blogPost, name="blogPost"),
]
