from django.shortcuts import render
from .models import Person, Car
from .serializers import PersonSerializer, CarSerializer
from rest_framework import viewsets


class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
