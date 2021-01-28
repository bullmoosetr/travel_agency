from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from travel_agency_app.models import DestinationType, DangerLevel, Location, \
    TourPackage, TourCapacity, Destination, Availability, GeoLocation,OpenWeatherTempRanges

class GeoLocationSerializer(ModelSerializer):
    class Meta:
        model = GeoLocation
        fields='__all__'

class WeatherRangeSerializer(ModelSerializer):
    class Meta:
        model= OpenWeatherTempRanges
        fields='__all__'

class CapacitySerializer(ModelSerializer):
    capacity = serializers.IntegerField()
    class Meta:
        model=TourCapacity
        fields='__all__'

class AvailabilitySerializer(ModelSerializer):
    class Meta:
        model=Availability
        fields='__all__'

class DestionationTypeSerializer(ModelSerializer):
    class Meta:
        model = DestinationType
        fields='__all__'

class DangerScoreSerializer(ModelSerializer):
    class Meta:
        model = DangerLevel
        fields='__all__'

class LocationSerializer(ModelSerializer):
    geolocation = GeoLocationSerializer()
    destination = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model= Location
        fields='__all__'

class DestinationSerializer(ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Destination
        fields='__all__'

class TourPackageSerializer(ModelSerializer):
    availability = AvailabilitySerializer(many=True)
    capacity = CapacitySerializer(read_only=True) 
    destination = DestinationSerializer(many=True, read_only=True)

    class Meta:
        model = TourPackage
        fields='__all__'