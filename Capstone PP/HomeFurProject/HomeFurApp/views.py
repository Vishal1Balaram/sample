from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomerAuth
from .serializers import CustomerSerializer
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.
class AlldataView(APIView):
    def get(self, request, *args, **kwargs):
        results = CustomerAuth.objects.all()
        serializer = CustomerSerializer(results, many=True)
        return Response ({'status': 'Success', 'Customers_data': serializer.data}, status=200)


class LoginView(APIView):
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        serializer = CustomerSerializer(data=request.data)
        username_password = request.data
        print(username_password.get('password'))
        # compare = CustomerAuth.objects.all('username')
        # print(compare)
        # print(username_password)
        
class RegisterView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response ({'status': 'Registered Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        else: 
            return Response({'status': 'Error', 'data': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)



















































