from dotenv import load_dotenv
import requests
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city="Kolkata"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("Get current weather conditions\n")
    city=input("Please enter the city name:\n")

    if not bool(city.strip()):
        city='Kolkata'
    
    weather_data=get_current_weather(city)
    print("\n")
    pprint(weather_data)
