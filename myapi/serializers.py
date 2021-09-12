from rest_framework import serializers

from .models import Vehicles

class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('unit', 'mileage', 'manufacturer', 'status', 'day')