from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm)
    role=forms.ChoiceField(choices=CustomerUser.ROLE_CHOICES,required=True)

    class Meta:
        model=CustomUser
        fields=UserCreationForm.Meta.fields +('role',)
        