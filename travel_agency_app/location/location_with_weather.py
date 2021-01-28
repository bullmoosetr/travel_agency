from .weather_api.get_weather import build_weather_dict
from ..models import Location, OpenWeatherTempRanges

def get_capitals_with_current_weather():
    # Cache the Results in Memory to avoid any db hits
    capitals = Location.objects.filter(is_capital=True).select_related('geolocation')
    # Need To Dicts
    # One Containing the List of Capitalos and Temps
    # One that holds the ranges for comparing
    # iterate through the list of ranges
    # When a Range fits, the Capital is appended to to dict
    # Access Dict two by
    # weather_ranges_dict {[0, 10]: "0-10"}
    # response_list {"0-10":[]}

    # Get the Ranges from the DB
    weather_ranges = OpenWeatherTempRanges.objects.all()

    weather_ranges_dict = {str(rng.weather_range):"-".join(list(map(str, rng.weather_range)))for rng in weather_ranges}
    weather_ranges_list = [rng.weather_range for rng in weather_ranges]
    # This is the dict we will serialize as a JSON response in the view
    response_list = {"-".join(list(map(str, rng.weather_range))):[] for rng in weather_ranges}

    # Now We Need to Get the Current Weather For Each Capital
    # Dict will be {bogota:temperature_celcius}
    capitals_and_temps = {
        capital.location_name:build_weather_dict(lat=capital.geolocation.latitude, lng=capital.geolocation.longitude) for capital in capitals
        }
    for key, value in capitals_and_temps.items():
        # Capital, Temp
        # Find a temp within the range of the stored ranges
        # Iterate of the list until we find a range that matches and we use that to find the entry in the the repnse list
        # We use that for comparison, I think that should all be O(1) with the O(n) operation iterating the list of ranges
        for rng in weather_ranges_list:
            if rng[0] <= value['current_temperature'] <= rng[1]:
                # Access the Weather Dict to get the Range String We Want
                temp = weather_ranges_dict[str(rng)]
                capital_with_forecast = {key:value['current_weather']}
                response_list[temp].append(capital_with_forecast)
    return response_list
    
