from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    name=models.CharField(max_length=30)
    # slug=models.SlugField()
    address=models.TextField(max_length=None)
    phone=models.CharField(max_length=10)

    gender=models.CharField(max_length=6)
    # thumb=models.ImageField(default='default.png',blank=True)
    age=models.PositiveSmallIntegerField()
    weight=models.FloatField()
    height=models.FloatField()
    email=models.EmailField()
    profilepic=models.ImageField(default='default.png')
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    # add thumbnail and author later
class UserFile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.document.name
