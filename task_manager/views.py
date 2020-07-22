from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response

from task_manager.serializer import UserSerializer, UserLoginSerializer


class UserSignUpViewSet(viewsets.ModelViewSet):
    """
    Creates the user
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {}
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                response['token'] = token.key
                response['status'] = 'success'
                return Response(response, status=HTTP_200_OK)
            response['status'] = 'failed'
            return Response(response, status=HTTP_401_UNAUTHORIZED)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )
