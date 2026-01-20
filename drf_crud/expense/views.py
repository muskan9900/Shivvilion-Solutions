from django.shortcuts import render
from .models import Transaction
from rest_framework.response import Response
from .serialization import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.

# api created through decorator
@api_view()
def get_transaction(request):
    queryset= Transaction.objects.all()
    serializer= TransactionSerializer(queryset,many=True)
    
    # returning Response 
    return Response({
        "data": serializer.data
    }) 

# creating api from view class
class TransactionAPI(APIView):

def get_transaction(request):
    queryset= Transaction.objects.all()
    serializer= TransactionSerializer(queryset,many=True)
    
    # returning Response 
    return Response({
        "data": serializer.data
    }) 

def get(self,request):
        return Response({
            "message": "this is a get method"
        })
        
def post(self,request):
        
        return Response({
            "message": "this is a post method"
        })
    
def put(self,request):
        return Response({
            "message": "this is a put method"
        })
    
def patch(self,request):
        return Response({
            "message": "this is a patch method"
        })
    
def delete(self,request):
        return Response({
            "message": "this is a delete method"
        })
