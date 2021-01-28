import os
from dotenv import load_dotenv

# Import Settings from .env
load_dotenv()

OPEN_WEATHER_API_KEY=os.getenv('OPEN_WEATHER_API_KEY')

GOOGLE_PLACES_API_KEY=os.getenv('GOOGLE_PLACES_API_KEY')