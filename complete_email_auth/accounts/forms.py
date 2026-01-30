from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Create password"}))

class VerifyOTPForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}))
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={"placeholder": "Enter OTP"}))

class ResendOTPForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}))
