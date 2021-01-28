import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q
from django.core.cache import cache
from django.http import (Http404, HttpResponse, HttpResponseNotAllowed,
                         HttpResponseNotFound, JsonResponse)
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .destination.serializers import (AvailabilitySerializer, CapacitySerializer, 
                                      DangerScoreSerializer,
                                      DestinationSerializer,
                                      DestionationTypeSerializer, GeoLocationSerializer,
                                      TourPackageSerializer,
                                      LocationSerializer,
                                      WeatherRangeSerializer)

from .location.location_with_weather import get_capitals_with_current_weather
from .models import (Availability, DangerLevel, Destination, DestinationType, Location,
                     OpenWeatherTempRanges, TourCapacity, TourPackage, GeoLocation)


@api_view(['GET'])
def get_capital_weather_report(request):
    #from IPython import embed; embed()
    cache_key = 'weather_report'
    cache_time = 900
    weather_report = cache.get(cache_key, {})
    if not weather_report:
        weather_report = get_capitals_with_current_weather()
    cache.set(cache_key, "weather_report", cache_time)
    return JsonResponse(weather_report)

# Weather Ranges
class WeatherRangesViewSet(generics.ListCreateAPIView):
    serializer_class = WeatherRangeSerializer
    queryset = OpenWeatherTempRanges.objects.all()

class WeatherRangesDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WeatherRangeSerializer
    queryset = OpenWeatherTempRanges.objects.all()

# Destination Type
class DestinationTypeViewSet(generics.ListCreateAPIView):
    serializer_class = DestionationTypeSerializer
    queryset = DestinationType.objects.all()

class DestinationTypeDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DestionationTypeSerializer
    queryset = DestinationType.objects.all()

# DangerScore
class DangerScoreViewSet(generics.ListCreateAPIView):
    serializer_class = DangerScoreSerializer
    queryset = DangerLevel.objects.all()

class DangerScoreDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DangerScoreSerializer
    queryset = DangerLevel.objects.all()

# Tour Package
class TourPackageViewSet(generics.ListCreateAPIView):
    serializer_class = TourPackageSerializer
    queryset = TourPackage.objects.all()

class TourPackageDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TourPackageSerializer
    queryset = TourPackage.objects.all()

class AvailableTourPackages(generics.ListAPIView):

    model = TourPackage
    serializer_class = TourPackageSerializer

    def get_queryset(self):
        queryset = TourPackage.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            queryset = TourPackage.objects.filter(Q(availability__availability__gte=start_date)&Q(availability__availability__lte=end_date))
        return queryset
    
    filter_backends = [DjangoFilterBackend]

#Destination
class DestinationViewSet(generics.ListCreateAPIView):
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()

class DestinationViewSetDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()

#Availability
class AvailabilityViewSet(generics.ListCreateAPIView):
    serializer_class = AvailabilitySerializer
    queryset = Availability.objects.all()

class AvailabilityDetailsViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = AvailabilitySerializer
    queryset = Availability.objects.all()

# Location
class LocationViewSet(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDetailViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

# GeoLocation
class GeoLocationViewSet(generics.ListCreateAPIView):
    serializer_class = GeoLocationSerializer
    queryset = GeoLocation.objects.all()

class GeoLocationDetailViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = GeoLocationSerializer
    queryset = GeoLocation.objects.all()

# Capacity
class CapacityViewSet(generics.ListCreateAPIView):
    serializer_class = CapacitySerializer
    queryset = TourCapacity.objects.all()

class CapacityDetailsViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = CapacitySerializer
    queryset = TourCapacity.objects.all()