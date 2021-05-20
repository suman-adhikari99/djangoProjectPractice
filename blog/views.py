from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse, request
#added manually
from datetime import datetime
from blog.models import contact
from django.contrib import messages
from django.core.paginator import Paginator,  PageNotAnInteger



# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def Contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contactsubmit=contact(name=name,email=email,phone=phone,desc=desc)
        contactsubmit.save()
        Message= messages.success(request, ' your form is submited')

    return render(request, 'contact.html')


def adds(request):
    return render(request,'add.html')

def add(request):
    vum1=request.GET['num1']
    vum2=request.GET['num2']
    result=vum1+vum2
    return render(request,'addresult.html' , {'result':result})


def post_list(request):
    post=contact.objects.all()
    p = Paginator(post, 2)
    page_number = request.GET.get('page')
    posts = p.get_page(page_number)
    print(post)
    
    return render(request,'post_list.html',{'posts':posts})

