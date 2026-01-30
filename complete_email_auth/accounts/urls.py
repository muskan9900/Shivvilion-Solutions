# accounts/urls.py
from django.urls import path
from .views import RegisterAPI,VerifyOTP,ResendOTP
from .import views_ui

urlpatterns = [
    #  API endpoints
    path("register/", RegisterAPI.as_view(), name="api_register"),
    path("verify-otp/", VerifyOTP.as_view(), name="api_verify_otp"),
    path("Resend-otp/", ResendOTP.as_view(), name="api_resend_otp"),
    

    #  (templates)
    path("auth/register/", views_ui.register_page, name="register_page"),
    path("auth/verify/", views_ui.verify_page, name="verify_page"),
    path("auth/resend/", views_ui.resend_page, name="resend_page"),
    path("auth/verified/", views_ui.verified_page, name="verified_page"),
]
