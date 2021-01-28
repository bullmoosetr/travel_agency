from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.cache import cache
from travel_agency_app.location.weather_api.get_weather import build_weather_dict
from django.http import JsonResponse
from travel_agency_app.models import Location

# http://127.0.0.1:8000/weather_api/weather_report/?location=La Paz
# Weather Forecast for a Location
@api_view(['GET'])
def get_weather_forecast(request):
    #from IPython import embed; embed()
    location = request.GET.get('location', '')
    cache_key = (location).join("_")+ "_forecast"
    cache_time = 900
    weather = cache.get(cache_key, {})
    if weather:
        query = Location.objects.get(location_name=location)
        if query:
            weather = build_weather_dict(lat=query.geolocation.latitude, lng=query.geolocation.longitude)

    cache.set(cache_key, "weather", cache_time)
    return JsonResponse(weather)
    
#Current Weather
@api_view(['GET'])
def get_current_weather_report(request):
    #from IPython import embed; embed()
    location = request.GET.get('location', '')
    cache_key = (location).join("_")+ '_current'
    cache_time = 900
    weather = None#cache.get(cache_key, {})
    if not weather:
        query = Location.objects.get(location_name=location)
        if query:
            weather = build_weather_dict(lat=query.geolocation.latitude, lng=query.geolocation.longitude)
    cache.set(cache_key, "weather", cache_time)
    return JsonResponse(weather['current_weather'])