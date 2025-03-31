import os
import requests
import json
from dotenv import load_dotenv

def get_weather(city):
    """
    Get the weather for a given city using OpenWeatherMap API.

    Parameters:
        city (str): The name of the city to fetch the weather for.

    Returns:
        dict: A dictionary containing weather data for the city.

    Raises:
        ValueError: If the API key is not found in the environment variables.
        Exception: If there is an error fetching weather data or the response is invalid.
    """
    load_dotenv("intermediate/weatherapp/weatherapp.env")
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the OPENWEATHER_API_KEY environment variable.")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching weather data: {response.status_code} - {response.text}")
    
    data = response.json()
    if 'main' not in data:
        raise Exception("Invalid response from weather API.")
    
    return {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }

myCity = input("Enter the name of the city: ")
weather_data = get_weather(myCity)