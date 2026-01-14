from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.

def signupPage(request):
    if request.method =='POST':
        user= request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        if pass1 != pass2:
             return HttpResponse("your password doesn't match")
        else:
        # user created by User class
        # passing the variable in create_user()
            myUser= User.objects.create_user(email,user,pass1,pass2)
            myUser.save()
            return redirect('login')
        print(email,user,pass1,pass2)
    return render(request,"signup.html")

def loginPage(request):
    if request.method =='POST':
        user=request.POST.get("username")
        pass1=request.POST.get("password")
        Myuser=authenticate(useranme=user,password=pass1)
        if Myuser is not None:
            login(request,Myuser)
            return redirect('home')
    return render(request,"login.html")

def logoutPage(request):
    return redirect('logout')

@login_required
def homePage(request):
    return redirect(request,"home.html")