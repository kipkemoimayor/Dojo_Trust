from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=50)
    profile=models.ImageField(upload_to='profile/',default='user.png',blank=True)
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

CATEGORIES=(
    ('real','Real Estate'),
    ('cars','Automobile'),
    ('agri','Agriculture'),
    ('wear','Clothes'),
)

class Business(models.Model):
    company=models.CharField(max_length=50,blank=True)
    businesName=models.CharField(max_length=50)
    category=models.CharField(max_length=7,choices=CATEGORIES,default='select')
    image=models.ImageField(upload_to='business/',blank=True,default='user.png')
    description=models.TextField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    users=models.ForeignKey(Users,on_delete=models.CASCADE)

    def __str__(self):
        return self.businesName
    @classmethod
    def search_by_name(cls,name):
        results=cls.objects.filter(businesName__icontains=name)
        return results


class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    business=models.ForeignKey(Business,on_delete=models.CASCADE,blank=True)
    review=models.CharField(max_length=200,help_text='Leave a review')
    profile=models.ForeignKey(Users,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.review
