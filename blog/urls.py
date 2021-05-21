
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('services/',views.services,name="servies"),
    path('contact/',views.Contact,name="contact"),
    path('contact/contactsubmit/',views.Contact,name="contactsubmit"),
    path('add/',views.adds,name="addhtmlfile"),
    path('add/addResult/',views.add,name='addResult'),
    path("post_list/",views.post_list, name="post_list"),
    path('registration/',views.showformdata,name='showformdata'),
    path('modelform/',views.Contactform, name='Contactform'),
   
]
