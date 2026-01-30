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
    otp_attempts=models.PositiveBigIntegerField(default=0)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserManager()


    # displaying the model objects
    def name(self):
        return self.first_name +' ' + self.last_name
    
    def __str__(self):
        return self.email
    
# python shell check 

# from accounts.models import User
# u = User.objects.last()
# u.email, u.otp, u.otp_created_at

# for wrong otp check
# from accounts.models import User
# u = User.objects.get(email="muskanimtiaz003@gmail.com")
# u.otp_attempts

# quick check for otp created at time zone

# from django.utils import timezone
# from accounts.models import User

# u = User.objects.get(email="muskanimtiaz003@gmail.com")
# print("OTP:", u.otp)
# print("Created (IST):", timezone.localtime(u.otp_created_at))
# print("Now (IST):", timezone.localtime(timezone.now()))
