from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    '''
    course_choices=[
        ('dj','django'),
        ('py','python'),
        ('j','java'),
        ('ml','machineLeraning'),   
         ]
    course=models.CharField(max_length=100,choices=course_choices,default='django')
    '''
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
   


def __str__(self):
    return str.title


