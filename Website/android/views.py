from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Androidapp, User, AppDownload, Profile
from .serializers import AndroidAppSerializer, UserSerializer, AppDownloadSerializer

class AndroidAppViewSet(viewsets.ModelViewSet):
    queryset = Androidapp.objects.all()
    serializer_class = AndroidAppSerializer
    permission_classes = [IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AppDownloadViewSet(viewsets.ModelViewSet):
    queryset = AppDownload.objects.all()
    serializer_class = AppDownloadSerializer
    permission_classes = [IsAuthenticated]
class UserSignupView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

