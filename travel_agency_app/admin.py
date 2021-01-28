from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TourPackage)
admin.site.register(Destination)
admin.site.register(Location)
admin.site.register(GeoLocation)
admin.site.register(Availability)
admin.site.register(DestinationType)
admin.site.register(DangerLevel)
admin.site.register(OpenWeatherTempRanges)

