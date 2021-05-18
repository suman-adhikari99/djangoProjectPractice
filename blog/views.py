from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    return HttpResponse("hi")
def post(request):
    post= Post.objects.all()
    return render(request,'index.html',{"post":post})
    
