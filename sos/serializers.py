from rest_framework import serializers
from .models import SOSAlert, Location

class SOSSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()