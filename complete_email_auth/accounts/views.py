from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *
from .models import User
from .utils import make_otp_token,MAX_OTP_ATTEMPTS
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken

# Create your views here.
class RegisterAPI(APIView):
    # post means create action
    def post(self,request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save(is_verified=False)
                send_otp_via_email(user.email)  # saves otp in db
                otp_token = make_otp_token(user.email)  # expires in 5 minutes
                return Response({
                        "status": 200,
                        "message": "registration successful, check email",
                        "data": serializer.data,
                        "otp_token": otp_token
                    })

            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': serializer.errors,
            }) 
        except Exception as e:
            print(e)
            return Response(
        {"error": str(e)})
    
class VerifyOTP(APIView):
    def post(self, request):
            
        serializer = verifyAccountSerializer(data=request.data)
        if not serializer.is_valid():
                return Response({"status": 400, "message": "invalid data", "data": serializer.errors})

        email = serializer.validated_data["email"].strip().lower()
        otp = str(serializer.validated_data["otp"]).strip()
        otp_token = serializer.validated_data["otp_token"].strip()

        # token validations

        try:
            token = AccessToken(otp_token)
        except TokenError:
            return Response({"status": 400, "message": "OTP expired. Please resend OTP.", "data": {}})

        if token.get("purpose") != "otp_verify":
            return Response({"status": 400, "message": "Invalid token.", "data": {}})

        if token.get("email") != email:
            return Response({"status": 400, "message": "Token/email mismatch.", "data": {}})
        # user validations
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"status": 400, "message": "user not found", "data": {}})

        if user.is_verified:
            return Response({"status": 200, "message": "already verified", "data": {}})
        # limits attempts
        if user.otp_attempts >= MAX_OTP_ATTEMPTS:
            return Response({"status": 429, "message": "too many attempts. resend otp.", "data": {}})
        if not user.otp:
             return Response({"status": 400, "message": "otp missing. resend otp.", "data": {}})
        # match the otp 
        if str(user.otp).strip() != otp:
            user.otp_attempts += 1
            user.save(update_fields=["otp_attempts"])
            return Response({"status": 400, "message": "wrong otp", "data": {"attempts": user.otp_attempts}})
        # success if user get true
        user.is_verified = True
        user.otp = None
        user.otp_attempts = 0
        user.save(update_fields=["is_verified", "otp", "otp_attempts"])

        return Response({"status": 200, "message": "account verified", "data": {}})      
class ResendOTP(APIView):
    def post(self, request):

      try:
            serializer = ResendOtpSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({"status": 400, "message": "invalid data", "data": serializer.errors})

            email = serializer.validated_data["email"].strip().lower()
            user = User.objects.filter(email=email).first()

            if not user:
                return Response({"status": 400, "message": "user not found", "data": {}})

            if user.is_verified:
                return Response({"status": 400, "message": "already verified", "data": {}})
            
            send_otp_via_email(user.email)
            otp_token = make_otp_token(user.email)

            return Response({"status": 200, "message": "otp resent successfully", "otp_token": otp_token, "data": {}})
      except Exception as e:
            return Response({"error": str(e)})

            
      

    #   -----

