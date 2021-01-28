from django.db import models
from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField
from django.db.models import constraints
from datetime import datetime, date

def validate_format(value):
    if value.__format__ == "%Y-%m-%d":
        raise ValidationError(
            _('%(value)s is not in Y-M-D Format'),
            params={'value': value},
        )

# Models
class OpenWeatherTempRanges(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    weather_range = ArrayField(
        models.IntegerField(),
    )

class Location(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    location_name = models.CharField(max_length=50)
    is_capital = models.BooleanField()

    def __str__(self):
        return 'Location: %s, Capital: %s' % (self.location_name, self.is_capital)

class DestinationType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Type: %s, Description: %s' % (self.name, self.description)

class DangerLevel(models.Model):
    danger_score = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.danger_score)

class TourPackage(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    registries = models.IntegerField()
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return 'Name: %s, Price: %s,Description: %s , Persons Registered %s' % (self.name, self.price, self.description, self.registries)

class Destination(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    destination_name = models.CharField(max_length=50)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='destination',
    )
    danger_level = models.ManyToManyField(
        DangerLevel
    )
    destination_type = models.ManyToManyField(
        DestinationType
    )
    tour_package = models.ManyToManyField(
        TourPackage,
        related_name="destination",
    )

    def __str__(self):
        return '%s' % (self.destination_name)

class TourCapacity(models.Model):
    capacity = models.IntegerField()
    tour_package = models.OneToOneField(
        TourPackage,
        on_delete=models.CASCADE,
        related_name='capacity',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Capacity:%s' % (self.capacity)


class Availability(models.Model):
    availability = models.DateField(validators=[validate_format])
    tour_package = models.ManyToManyField(
        TourPackage,
        related_name='availability'
    )
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'availability_dates:%s' % (self.availability)



class GeoLocation(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return '%s %s' % (self.latitude, self.longitude)

@receiver(pre_save, sender=TourPackage)
def validate_capacity(sender, instance, **kwargs):
    if instance.registries > instance.capacity.capacity:
        raise ValidationError(
            _("Please Verfiy the Capacity and Persons Registered")
        )


