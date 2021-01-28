import requests
import json
from travel_agency_app.contstants import GOOGLE_PLACE_BASE_URL
from travel_agency_app.settings import GOOGLE_PLACES_API_KEY

def get_location_data(location_request):
    if location_request['location']:
        params = {"input":location_request['location'], "inputtype":"textquery", "fields":"formatted_address,name,geometry","key":GOOGLE_PLACES_API_KEY}
        return requests.get(GOOGLE_PLACE_BASE_URL, params=params).json()

def parse_location_details(location_details):
    # Parse out the Candidates
    # This is Meant to Provide Help when looking for location details
    return [i for i in location_details.get('candidates')]