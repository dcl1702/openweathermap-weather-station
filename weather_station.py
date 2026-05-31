#DSC 510
#Week 12
#Final Class Project 12.1
#Author: Dong Lee
#03/02/2025
#Purpose: Interact with a web service to obtain weather data.  Prompt the
# user for their city or zip code and request weather forecast data from
# openweathermap.org and display the weather information in a readable format
# to the user.

import requests
from datetime import date
import textwrap
import os

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')


#set up API key to use for api calls.


def handle_api_request(url):
    #get response from the api call with the url and return json data.
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}\n")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}\n")
    except requests.exceptions.Timeout as time_err:
        print(f"Timeout error occurred: {time_err}\n")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}\n")
    except KeyError as key_err:
        print(f"Unexpected response structure: {key_err}\n")
    except Exception as err:
        print(f"An unexpected error occurred: {err}\n")

    #return empty dict if api exception occurs
    return {}


def get_lat_lon(user_input):
    #check if input is zip code or city name and call api accordingly
    if user_input.isdigit():
        # zip code
        url = (f"http://api.openweathermap.org/geo/1.0/zip?zip={user_input},"
               f"US&appid={API_KEY}")
        loc_data = handle_api_request(url)
        input_format = 'zip'
    else:
        #city name
        url = (f"http://api.openweathermap.org/geo/1.0/direct?q={user_input},"
               f"US&limit=5&appid={API_KEY}")
        loc_data = handle_api_request(url)
        input_format = 'city'

    try:

        # check api did not return empty data
        if not loc_data:
            raise ValueError("Empty Response")
        else:
            #get first entry if city name was the input. city name api
            # returns a dict and zip code api returns a list.
            if input_format == 'city':
                lat, lon = loc_data[0]['lat'], loc_data[0]['lon']
            else:
                lat, lon = loc_data['lat'], loc_data['lon']

            return lat,lon
    except (ValueError, IndexError, TypeError) as e:
        print("Data not available with the given location. Please enter "
              "valid city name or "
              "zip "
              "code.\n")

    #return None,None if exception occurs.
    return None,None

def get_weather(lat, lon):
    #api call to get weather data from lat and lon.
    #use imperial units to get temp in F
    url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon="
           f"{lon}&units=imperial&appid={API_KEY}")
    weather_data = handle_api_request(url)

    try:
        if not weather_data:
            raise ValueError("Empty response")
        else:
            return weather_data

    except (ValueError,IndexError,TypeError) as e:
        print("Weather data not available with given latitude and longitude. "
              "Please enter "
              "valid city name or zip "
              "code.\n")

    return {}

def print_weather(weather_data):
    #parse json and assign data to variables to print.
    city_name = weather_data['name']
    weather_desc = weather_data['weather'][0]['description']
    city_temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    temp_min, temp_max = weather_data['main']['temp_min'],weather_data[
        'main']['temp_max']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    cloud_cover = weather_data['clouds']['all']
    today = date.today()

    #print a weather report.
    print(textwrap.dedent(f"""
    Welcome to Lee's weather station!
    Date: {today}
    
    Today's weather in {city_name}:
        It is currently {city_temp} degrees F and feels like {feels_like} 
        degrees F.
        The minimum temperature is {temp_min} degrees F and the maximum 
        temperature is {temp_max} degrees F.
        The current weather condition is {weather_desc}, with cloud coverage of 
        {cloud_cover}%.
        The pressure is {pressure} hPa and humidity is {humidity}%.
        
        Please come back again for tomorrow's weather!
    """))

def main():
    sentinel = 'exit'

    while True:
        try:
            #ask for user input. User can either enter a city name with state
            # or zip code. Providing example for easier understanding.
            print("Please enter city name and state name, or zip code you "
                  "would like to know the weather of. or enter 'exit' to exit.")
            user_input = input("Input example: Seattle, WA / "
                               "12345 "
                               "\n").strip()

            #detect sentinel value and exit
            if user_input.lower() == sentinel:
                break

            #call get_lan_lon to get latitude and longitude of given location.
            if not user_input == '':
                lat,lon = get_lat_lon(user_input)
            else:
                raise ValueError('empty string')

            #if lat and lon is not None, call get_weather to get weather data.
            if lat and lon:
                weather_data = get_weather(lat,lon)
                if weather_data:
                    print_weather(weather_data)

        except ValueError as e:
            print(f"Value error, {e}. Please enter valid city name or zip "
                  f"code.\n")


if __name__ == "__main__":
    main()

