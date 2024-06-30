import os

import requests

API_KEY = open('API_KEY', 'r').read()


def get_weather(city):
    base = 'http://api.openweathermap.org/data/2.5/weather?'
    url = base + '&appid=' + API_KEY + '&q=' + city

    response = requests.get(url).json()

    temp_k = response['main']['temp']
    temp_c = temp_k - 273.15
    humidity = response['main']['humidity']
    pressure = response['main']['pressure']
    wind = response['wind']['speed']

    return temp_c, humidity, pressure, wind


print(get_weather('Cairo'))
