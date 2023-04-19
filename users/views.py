from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import UserSerializer
from django.contrib.auth.hashers import check_password
import jwt
from datetime import datetime, timedelta 
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        # print('REGISTER DATA->', request.data)
        # Endpoint: Post /api/auth/register/
        user_to_add = UserSerializer(data=request.data)
        if user_to_add.is_valid():
            user = user_to_add.save()
            return Response({"message": "User registered successfully", "user": UserSerializer(user).data}, status=201)
        else:
            return Response(user_to_add.errors, status=400)


class LoginView(APIView):
    # Endpoint: Post /api/auth/login/
    def post(self, request):
        print('REQUEST DATA ->', request.data)
        email = request.data['email']
        password = request.data['password']
        user_to_login = User.objects.get(email=email)
        if not user_to_login.check_password(password):
            print('Password dont match')
            #raise permissionDenied('Unauthorized')
        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode({'sub': user_to_login.id, 'exp': int(dt.timestamp())}, settings.SECRET_KEY, algorithm='HS256')
        print('TOKEN',token)
        return Response({'message': f"Welcome,{user_to_login.username}",'token':token})
