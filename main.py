import os
import time
import playsound
import speech_recognition as rs
from gtts import gTTS


def speak(text):
    audio = gTTS(text=text, lang='en')
    audio.save('audio.mp3')
    playsound.playsound('audio.mp3')
    os.remove('audio.mp3')


speak('Hi, I am Marcy!, your virtual assistant!, how can I help you?')
