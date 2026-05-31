# OpenWeatherMap API Weather Station

## Overview

This project is a Python command-line application that retrieves current weather data using the OpenWeatherMap API. The user can enter a U.S. city/state or ZIP code, and the program returns a readable weather summary for that location.

## Objective

The goal of this project was to practice working with a web service by requesting, parsing, and displaying real-time weather data.

## Features

- Accepts city/state or ZIP code input
- Uses OpenWeatherMap geocoding to find latitude and longitude
- Retrieves current weather data
- Displays temperature, feels-like temperature, weather condition, cloud coverage, pressure, and humidity
- Handles invalid inputs and API request errors

## Tools Used

- Python
- requests
- OpenWeatherMap API
- JSON parsing

## How It Works

1. The user enters a city/state or ZIP code.
2. The program converts the location into latitude and longitude.
3. The program requests current weather data from OpenWeatherMap.
4. The JSON response is parsed.
5. A readable weather report is printed for the user.

## Key Skills Demonstrated

- API integration
- JSON parsing
- User input handling
- Error handling
- Command-line application design
- Python function organization

## API Key Setup

This project requires an OpenWeatherMap API key. Store the key as an environment variable named:

OPENWEATHERMAP_API_KEY

## Future Improvements

- Move API key to an environment variable
- Add Celsius/Fahrenheit unit selection
- Support international locations
- Add multi-day forecast data
- Convert the script into a web app