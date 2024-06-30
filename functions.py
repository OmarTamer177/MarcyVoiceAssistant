import datetime
import os
import pyjokes
import requests
import wikipediaapi
import pywhatkit as pwk
from contacts import contacts

WEATHER_API_KEY = open('API_KEY', 'r').read()

programs = {
    'discord': '\"C:\\Users\\Otame\\AppData\\Local\\Discord\\app-1.0.9152\\Discord.exe\"',
    'notepad': '\"C:\\Program Files\\Notepad++\\notepad++.exe\"',
    'chrome': '\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"',
    'krita': '\"C:\\Program Files\\Krita (x64)\\bin\\krita.exe"',
    'aseprite': '\"C:\\Program Files\\Aseprite\\Aseprite.exe\"',
}


def get_weather(city: str):
    base = 'http://api.openweathermap.org/data/2.5/weather?'
    url = base + '&appid=' + WEATHER_API_KEY + '&q=' + city

    response = requests.get(url).json()

    temp_k = response['main']['temp']
    temp_c = temp_k - 273.15
    humidity = response['main']['humidity']
    pressure = response['main']['pressure']
    wind = response['wind']['speed']

    return temp_c, humidity, pressure, wind


def get_time():
    return datetime.datetime.now().strftime("%H:%M")


def get_date():
    return datetime.datetime.now().strftime("%A, %d %B %Y")


def get_summary(topic: str):
    wiki = wikipediaapi.Wikipedia('Marcy (nowhere@nowhere.com)', 'en')
    page = wiki.page(topic)
    summary = page.summary.split('.\n')
    return summary


def google_search(topic: str):
    pwk.search(topic)


def open_yt_video(topic: str):
    pwk.playonyt(topic)


def take_screenshot():
    pwk.take_screenshot("ss" + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))


def open_program(program: str):
    os.startfile(programs[program])


def get_joke():
    joke = pyjokes.get_joke(language='en')
    return joke


def send_msg(contact: str, msg: str):
    # Send msg to a contact using phone number
    pwk.sendwhatmsg_instantly(contacts[contact], msg, tab_close=True)
    # Delete the db file (no need for it)
    os.remove("PyWhatKit_DB.txt")


