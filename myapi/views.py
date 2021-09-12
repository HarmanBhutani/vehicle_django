from django.shortcuts import render
from rest_framework import viewsets

from .serializers import VehiclesSerializer
from .models import Vehicles


class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all().order_by('day')
    serializer_class = VehiclesSerializer

class DistanceViewSet(viewsets.ModelViewSet):
        queryset = Vehicles.objects.filter()
        serializer_class = VehiclesSerializer


# Create your views here.
