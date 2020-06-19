# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    UserId = models.IntegerField(blank=True)
    email=models.CharField(max_length=30,blank=True)
    MobileNumber=models.CharField(max_length=12)
    address = models.CharField(max_length=200,blank=True)

    def __str__(self):
      return str(self.user.id)+" "+str(self.user.username)
