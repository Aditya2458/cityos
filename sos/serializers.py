from rest_framework import serializers
from .models import SOSAlert, Location

class SOSSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'timestamp']


class SOSAlertSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = SOSAlert
        fields = ['id', 'user', 'status', 'created_at', 'location']