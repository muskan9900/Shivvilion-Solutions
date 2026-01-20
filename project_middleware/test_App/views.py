from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from test_App.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.

User= get_user_model()
def login_view(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            # redirects to home page after login
            return redirect('home')
    return render(request,'login.html')

def home_view(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    # redirect to login page after logout
    return render(request,'home.html')

def signup_view(request):
    if request.method=='POST':
        print(request.POST['username'])
        print(request.POST['password'])
        print(request.POST['role'])
        form=CustomUserCreationForm(request.POST)
        print(form.data)
        print(form.errors)
        if form.is_valid():
           print("valid")
           form.save()
           return redirect('login')
    else:
        form=CustomUserCreationForm()
        print("HI")
    return render(request,'sign.html',{'form': form})

def teacher_home(request):
    print("Welcome Teacher")
    return render(request,'teacher.html')

def student_home(request):
    print("Welcome Students")
    return render(request,'student.html')

def principal_home(request):
    print("Welcome Principal")
    return render(request,'principal.html')


