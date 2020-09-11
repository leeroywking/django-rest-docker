from django.shortcuts import render
from rest_framework import generics
from .serializer import CarSerializer
from .models import Cars

# Create your views here.


class CarList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
