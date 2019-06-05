from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=50)
    profile=models.ImageField(upload_to='profile/',blank=True)
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)



class Business(models.Model):
    businesName=models.CharField(max_length=50)
    image=models.ImageField(upload_to='business/',blank=True)
    description=models.TextField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    users=models.ForeignKey(Users,on_delete=models.CASCADE)

class Rate(models.Model):
    pass
