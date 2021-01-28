"""travel_agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, re_path
from travel_agency_app import views
from weather_api.views import get_weather_forecast, get_current_weather_report
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('admin/', admin.site.urls),

    path('locations/', views.LocationViewSet.as_view(), name='locations'),
    path('location/<int:pk>/', views.LocationDetailViewSet.as_view(), name='location'),

    path('geolocations/', views.GeoLocationViewSet.as_view(), name='geolocations'),
    path('geolocation/<int:pk>/', views.GeoLocationDetailViewSet.as_view(), name='location'),

    path('weather_ranges/', views.WeatherRangesViewSet.as_view(), name='weather_ranges'),
    path('weather_range/<int:pk>/', views.WeatherRangesDetailViewSet.as_view(), name='weather_range'),

    path('get_capitals_weather_report/', views.get_capital_weather_report),

    path('destination_types/', views.DestinationTypeViewSet.as_view(), name='destination_types'),
    path('destination_type/<int:pk>/', views.DestinationTypeDetailViewSet.as_view(), name='destination_type'),

    path('danger_scores/', views.DangerScoreViewSet.as_view(),name='danger_scores'),
    path('danger_score/<int:pk>/', views.DangerScoreDetailsViewSet.as_view(),name='danger_score'),

    path('tour_packages/', views.TourPackageViewSet.as_view(), name='tour_packages'),
    path('tour/<int:pk>/', views.TourPackageDetails.as_view(), name='tour'),
    re_path('available_tours/', views.AvailableTourPackages.as_view(), name='available_tours'),

    path('destinations/', views.DestinationViewSet.as_view(), name='destinations'),
    path('destination/<int:pk>/', views.DestinationViewSetDetails.as_view(),name='destinations'),
    
    path('availability_dates/', views.AvailabilityViewSet.as_view(),name='availability_dates'),
    path('availability_date/<int:pk>/', views.AvailabilityDetailsViewSet.as_view(),name='availability_date'),

    re_path('weather_api/weather_report/', get_weather_forecast),
    re_path('weather_api/current_weather/', get_current_weather_report)
    #path('destination/', include('travel_agency_app.destination.urls'))
    
]

