from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers.common import UserSerializer 

#Register route 
class RegisterView(APIView): 
    def post (self, request):
        print('REGISTER DATA->', request.data)
        user_to_add = UserSerializer(data=request.data)
        user_to_add.is_valid(raise_exception=True)
        return Response('Register Route Hit')
