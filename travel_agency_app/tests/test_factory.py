from django.test import TestCase
from travel_agency_app.models import Availability, Location, GeoLocation, TourCapacity, TourPackage

class LocationTestCase(TestCase):
    def setUp(self):
        loc = Location.objects.create(location_name="north pole", is_captial=True)
        GeoLocation.objects.create(latitute=10.4805937, longitude=-66.90360629999999, location=loc)
    
    def test_location_model(self):
        north_pole = Location.objects.get(location_name="north pole")
        lat = north_pole.geolocation.latitude
        self.assertEqual(north_pole.location_name, "north pole")
        self.assertEqual(lat, 10.4805937)

class TourPackageTestCase(TestCase):
    def setUp(self):
        tour = TourPackage.objects.create(name='Arctic Adventure', description='Lets freeze!', price=3000, registries=15)
        TourCapacity.objects.create(capacity=20, tourpackage=tour)
        available =Availability.objects.create(availability="2021-07-05")
        available.add(tour)
    
    def test_tour_package_model(self):
        arctic = TourPackage.objects.get(name='Arctic Adventure')
        self.assertNotEqual(arctic.name, "Arctic")
        self.assertEqual(arctic.availability.availability, "2021-07-05")