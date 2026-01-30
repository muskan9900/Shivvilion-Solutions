# importing model default user model

from django.contrib.auth.models import User 
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed 
from django.dispatch import receiver
# model signals 
from django.db.models.signals import pre_init, pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate

# using decorators 
@receiver(user_logged_in, sender=User)
def login_success(sender,request,user,**kwargs):
    print("----------")
    print("Logged in signal ....Run Intro.")
    print("Sender:", sender)
    print("Request:", request)
    print("User:",user)
    print("User Password:", user.password)
    print(f'kwargs:{kwargs}')

# by using init file
# user_logged_in.connect(login_success,sender=User)

# creating logout 

@receiver(user_logged_out, sender=User)
def logout_success(sender,request,user,**kwargs):
    print("----------")
    print("Logged out signal ....Run Outro.")
    print("Sender:", sender)
    print("Request:", request)
    print("User:",user)
    print("User Password:", user.password)
    print(f'kwargs:{kwargs}')

# creating login failed

@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("----------")
    print("Login failed .....")
    print("Sender:", sender)
    print("credentials:", credentials)
    print("Request:", request)
    print(f'kwargs:{kwargs}')