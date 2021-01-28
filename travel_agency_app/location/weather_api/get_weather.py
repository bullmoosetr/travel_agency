import requests

from ...settings import OPEN_WEATHER_API_KEY
from ...contstants import OPEN_WEATHER_CURRENT_BASE_URL, OPEN_WEATHER_FORECAST_BASE_URL

def get_current_weather(lat, lng):
    #api.openweathermap.org/data/2.5/weather?
    params = {"lat":lat, "lon":lng, "units":"metric","appid":OPEN_WEATHER_API_KEY}
    return requests.get(OPEN_WEATHER_CURRENT_BASE_URL, params=params).json()

def get_weather_forecast(lat, lng):
    params = {"lat":lat, "lon":lng, "units":"metric","appid":OPEN_WEATHER_API_KEY}
    return requests.get(OPEN_WEATHER_FORECAST_BASE_URL, params=params).json()

def build_weather_dict(lat, lng):
    current_weather = get_current_weather(lat=lat, lng=lng)
    weather_forecast = get_weather_forecast(lat=lat, lng=lng)
    weather_dict = {}
    if current_weather:
        weather_dict['current_temperature'] = current_weather['main']['temp']
        weather_dict['current_weather'] = current_weather['main']
    if weather_forecast:
        weather_dict['forecast'] = weather_forecast['list']
    return weather_dict