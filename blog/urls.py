from blog.models import Post
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name="home"),
    path("blog/",views.post,name="Post"),
]
