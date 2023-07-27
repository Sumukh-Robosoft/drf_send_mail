from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .manager import UserManager



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp_mail = models.CharField(max_length=4, null=True, blank=True)
    otp_sms = models.CharField(max_length=4, null=True, blank=True)
    phone=models.CharField(max_length = 10)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email

class Refresh_Token(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    refreshToken = models.CharField(max_length=500,unique=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
