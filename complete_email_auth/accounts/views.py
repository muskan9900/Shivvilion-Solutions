from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *

# Create your views here.
class RegisterAPI(APIView):
    # post means create action
    def post(self,request):
        try:
            data= request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                user_obj = serializer.save(is_verified=False)

                otp = send_otp_via_email(user_obj.email)
                user_obj.otp = otp
                user_obj.save(update_fields=["otp"])
                return Response({
                    "status": 200,
                    "message": "registration successful, check email",
                    "data": serializer.data,
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
     def post(self,request):
          try:
                data=request.data
                serializer=verifyAccountSerializer(data=data)

                if not serializer.is_valid():
                     return Response({
                          'status': 400, 
                          'message': "invalid data",
                     })

                email = serializer.validated_data['email'].strip().lower()
                otp = str(serializer.validated_data['otp']).strip()

                user = User.objects.filter(email=email)
                    #  if user not exist
                if not user.exists():
                           return Response({
                                      'status': 400,
                                     'message': 'something went wrong',
                                    'data': serializer.errors,
                                 })
                    
                if str(user[0].otp).strip() != otp:
                          return Response({
                                      'status': 400,
                                     'message': 'something went wrong',
                                    'data': 'wrong otp',
                            })
                user= user.first()
                user.otp= None
                user.is_verified= True
                user.save(update_fields=["is_verified", "otp"])
                return Response({   
                        'status': 200,
                        'message': 'account verified',
                        'data':{},
                     })
          
          except Exception as e:
                    print(e)
                    return Response(
                     {"error": str(e)})
    