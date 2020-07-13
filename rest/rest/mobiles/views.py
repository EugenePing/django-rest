from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Mobile
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class MobileCreateView(generics.CreateAPIView):
    serializer_class = MobileDetailSerializer


class MobileViewList(generics.ListAPIView):
    serializer_class = MobileListSerializer
    queryset = Mobile.objects.all()
    permission_classes = (IsAdminUser,)


class MobileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MobileDetailSerializer
    queryset = Mobile.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
