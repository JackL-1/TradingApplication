from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import UserSerializer
from django.contrib.auth.hashers import check_password
import jwt
from datetime import datetime, timedelta 
from django.conf import settings
from django.contrib import messages
from rest_framework import status
from decimal import Decimal
from django.db.models import Q

from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        print('REGISTER DATA->', request.data)
        user_to_add = UserSerializer(data=request.data)
        print('IS_VALID? ->', user_to_add.is_valid())
        if user_to_add.is_valid():
            user = user_to_add.save()
            print('USER DATA ->', UserSerializer(user).data)
            return Response({"message": "User registered successfully", "user": UserSerializer(user).data}, status=201)
        else:
            print('ERRORS ->', user_to_add.errors)
            return Response(user_to_add.errors, status=400)



class LoginView(APIView):
    # Endpoint: Post /api/auth/login/
    def post(self, request):
        if not request.data:
            return Response({'error': 'Request data is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        if 'username' not in request.data:
            return Response({'error': 'Username is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        if 'email' not in request.data:
            return Response({'error': 'Email is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        if 'password' not in request.data:
            return Response({'error': 'Password is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        user_to_login = User.objects.get(Q(email=email) | Q(username=username))
        if not user_to_login.check_password(password):
            print('Passwords dont match')
            #raise permissionDenied('Unauthorized')
        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode({'sub': user_to_login.id, 'exp': int(dt.timestamp())}, settings.SECRET_KEY, algorithm='HS256')
        print('TOKEN',token)
        return Response({'message': f"Welcome,{user_to_login.username}",'token':token})

    


class AddFunds(APIView):
    #Endpoint: 
    def get(self, request):
        return Response({"message": "Please enter the amount you wish to add to your funds."})
      #Endpoint: post /api/add_funds
    def post(self, request):
        amount = Decimal(request.data.get('amount'))
        if amount <= Decimal('0'):
            return Response({"error": "Please enter a positive amount."}, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        user.funds += amount
        user.save()
        return Response({"message": f"Successfully deposited {amount:.2f} to your account."}, status=status.HTTP_200_OK)


class RemoveFunds(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # Endpoint: DELETE /api/remove_funds
    def delete(self, request):
        amount = Decimal(request.data.get('amount'))
        if amount <= 0:
            return Response({"error": "Please enter a positive amount."}, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        if user.funds < amount:
            return Response({"error": "Insufficient funds."}, status=status.HTTP_400_BAD_REQUEST)
        user.funds -= amount
        user.save()
        return Response({"message": f"{amount:.2f} Successfully withdrawn."}, status=status.HTTP_200_OK)


class ToTheMoonView(APIView):
    def get(self, request):
        data = {'message': 'To the moon!'}
        return Response(data)