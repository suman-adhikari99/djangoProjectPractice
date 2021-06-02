
from os import name
from django.utils import regex_helper, timezone

from django.http import HttpResponse
from .models import Post,form,Comment, blogcomment
from django import forms
from .forms import PostForm, DocumentForm,Subscribe,CommentForm
from django.shortcuts import redirect, render, get_list_or_404,get_object_or_404
from django.core.paginator import Paginator , PageNotAnInteger

# Create your views here.
def home(request):
    return render(request,'home.html')

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)
    print(paginator.num_pages)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
        print(posts)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'post_list.html', {'page':page, 'posts':posts})




def post_new(request,id=0):
    if request.method == "POST":
        if id==0:
            form = PostForm(request.POST)
        else:
            obj=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=obj)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()    
            return redirect('post_list')
            
    else:
        if id==0:
            form = PostForm()
            return render(request, 'post_new.html', {'form':form})
        else:
            obj=Post.objects.get(pk=id)
            form=PostForm(instance=obj)
            return render(request,'post_new.html', {'form':form})


            
def upload(request):
    if request.method=="POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form=DocumentForm()
    return render(request, 'form_upload.html',{'form':form})




# added for django mail sending   
from firstproject.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail, send_mass_mail
import imghdr

def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST,request.FILES)
        subject = 'Welcome to Achievers Group'
        message = 'You are viewing demo'
        recepient = str(sub['Email'].value())
           
        print(recepient)
        send_mail(subject,message,EMAIL_HOST_USER,[recepient], fail_silently = False)
        if sub.is_valid():
            name=sub.cleaned_data['name']
            email=sub.cleaned_data['Email']
            file=sub.cleaned_data['chooseFile']
            #print(name)
            #print(email)
            print(file)
            form1=form(email=email, name=name,file=file)
            form1.save()
        return render(request,'success.html',{'recepient': recepient})
       
        
    return render(request, 'email.html', {'form':sub})
   




def mailmass(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        recepient = str(sub['Email'].value())
        message1 = ('Subject here', 'Here is the message', EMAIL_HOST_USER, [recepient])
        message2 = ('Another Subject', 'Here is another message', EMAIL_HOST_USER, [recepient])
        send_mass_mail((message1, message2), fail_silently=False)
        
        print(recepient)
        #send_mail(subject,message,EMAIL_HOST_USER,[recepient], fail_silently = False)
        return render(request,'success.html',{'recepient': recepient})
    return render(request, 'email.html', {'form':sub})



from django.core.mail import EmailMessage
def attach(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Achievers Group'
        message = 'You are viewing demo'
        recepient = str(sub['Email'].value())
        print(recepient)
        file=open('D:/djangoproject/blog/templates/attach.html').read()
       
        #send_mail(subject,message,EMAIL_HOST_USER,[recepient], fail_silently = False)
        email = EmailMessage('Hello', file, EMAIL_HOST_USER, [recepient])
        email.content_subtype='html'
        
        email.attach_file('D:/New folder/Capture.JPG')    
        email.send()
        
        return render(request,'success.html',{'recepient': recepient})
    return render(request, 'email.html', {'form':sub})
    
    
    
def post_detail(request, pk=0):
    post=Post.objects.get(pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None

    #Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post= post
            new_comment.save()
        return redirect('/blog')
    else:

        comment_form = CommentForm()
        return render(request, 'post_detail.html', {'post':post, 'comments': comments, 'new_comment':new_comment,'comment_form':comment_form})
                                           

      
    
def postComment(request,id):
    post=Post.objects.get(pk=id)
    comments= blogcomment.objects.filter(post=post, parent=None)
    if request.method=="POST":
        comments= request.POST.get("comment")
        user=request.user  
        parentSno= request.POST.get('parentSno')

        posts=Post.objects.get(pk=id)
        if parentSno=="":
            comment=blogcomment(comment= comments, user=user, post=post)
            comment.post= post
            comment.save()
            return render(request,'post_detail.html', {'blogcomment':comment,"post":posts,'blogcommen':comments})
        else:
            parent= blogcomment.objects.get(sno=parentSno)
            comment=blogcomment(comment= comments, user=user, post=post , parent=parent)
            comment.save()
            replies= blogcomment.objects.filter(post=post).exclude(parent=None)
            return render(request,'post_detail.html', {'replycomment':comment,"post":posts,'replie':replies})
           
        
    if request.method=='GET':
       
        return render(request,'post_detail.html',{'blogcommen':comments,'pos':post})


   

        
