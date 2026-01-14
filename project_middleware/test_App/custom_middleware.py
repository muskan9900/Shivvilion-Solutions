from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from test_App import views
from django.contrib.auth import get_user_model

User=get_user_model()

class CustomMiddle(MiddlewareMixin):
    def process_request(self,request):
        # checks if the request is for the login or logout views
        if request.path =='/login/':
            # handles login Logic
            print("Login Request")

        elif request.path == '/logout/':
            # handles logout Logic
            print("Logout Request")
        elif request.path =='/admin/':
            print("Admin")
        elif request.user.is_authenticated:
            role=request.user.role
            print(role)
            if role=='teacher' and not request.path.startswith('/teacher_home'):
                return redirect('teacher_home')
            
            elif role=='student' and not request.path.startswith('/student_home'):
                return redirect('student_home')
            elif role=='principal' and not request.path.startswith('/principal_home'):
                 return redirect('prinpal_home')                                            