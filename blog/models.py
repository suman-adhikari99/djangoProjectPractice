from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class contact(models.Model):

    name= models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.IntegerField()
    desc=models.TextField()


