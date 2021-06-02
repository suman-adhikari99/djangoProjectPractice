from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
  
    #path('post/new/post/new/',views.post_list, name="post_new"),
    path('home/',views.home, name="post_new"),
    path('post/new/<int:id>',views.post_new, name="post_new"),
    path('file_upload/' , views.upload, name="upload"),
    path('email/' , views.subscribe, name="subscribe"),
    path('mailmass/' , views.mailmass, name="mailmass"),
    path('attach/' , views.attach, name="attach"),
    path('postComment/<int:id>',views.postComment,name='postComment'),




]
