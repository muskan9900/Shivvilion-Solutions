from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .manager import UserManager


# Create your models here.

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    is_verified= models.BooleanField(default=False)
    otp=models.CharField(max_length=6, null=True,blank=True)
    otp_created_at=models.DateTimeField(null=True,blank=True)
    otp_attempts=models.PositiveBigIntegerField(default=0)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserManager()


    # displaying the model objects
    def name(self):
        return self.first_name +' ' + self.last_name
    
    def __str__(self):
        return self.email