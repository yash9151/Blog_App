from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.blogHome, name="blogHome"),
    # API to post a comment
    path("postComment", views.postComment, name="postComment"),
    path('<str:slug>/', views.blogPost, name="blogPost"),
]
