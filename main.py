import sys
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit as pwk
import pyjokes
import wikipediaapi
from functions import *


class Assistant:
    def __init__(self, wake_word):
        # Initialize the Speech Recognizer and Text To Speech engines
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

        # Give Marcy a suitable voice
        voices = self.tts_engine.getProperty('voices')
        self.tts_engine.setProperty('voice', voices[1].id)

        # Wake word
        self.wake_word = wake_word

    # Function to convert text to speech
    def talk(self, text):
        print(text)                   # Print the text along
        self.tts_engine.say(text)     # Add text to the queue to be said
        self.tts_engine.runAndWait()  # Say everything in the queue

    # Function to take voice input
    def take_command(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)
                command = command.lower()
        except Exception as e:
            print(e)
            return "commandException"
        return command

    # Function to take text input (for testing purpose)
    def take_command_text(self):
        command = input("Me: ")
        return command

    # Function to handle the commands
    def handle_command(self, command):
        # Exit the app
        if 'bye' in command or 'quit' in command or 'exit' in command or 'see you' in command:
            self.talk("See you soon!")
            sys.exit()
        # Getting the time in hours and minutes
        elif 'time' in command:
            self.talk("time is " + datetime.datetime.now().strftime("%H:%M"))
        # Getting today's date
        elif 'date' in command:
            self.talk(datetime.datetime.now().strftime("%A, %d %B %Y"))
        # 3shan el 3yal el 3beta (to be removed)
        elif 'i love you' in command or 'i like you' in command:
            self.talk("Unfortunately, I am a robot and I don't possess human emotions")
        elif 'joke' in command:
            joke = pyjokes.get_joke(language='en')
            self.talk("I have a good joke for you!")
            self.talk(joke + "\nha ha ha ha!!")
        elif 'wikipedia' in command or 'summary' in command:
            wiki_wiki = wikipediaapi.Wikipedia('Marcy (nowhere@nowhere.com)', 'en')
            page_py = wiki_wiki.page('Bill gates')
            self.talk(page_py.summary.split('.\n')[0])
        elif 'whatsapp' in command or 'message' in command:
            # Send msg to a group using group_id
            # pwk.sendwhatmsg_to_group_instantly("xxxx", "hello from python", tab_close=True)
            # Send msg to a phone number
            # pwk.sendwhatmsg_to_group_instantly("xxxx", "hello from python", tab_close=True)
            pass
        elif 'google' in command:
            pwk.search("minecraft")
        elif 'youtube' in command:
            pwk.playonyt("minecraft")
        elif 'screenshot' in command:
            pwk.take_screenshot("sc"+datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        elif 'weather' in command:
            print(command)   # get the weather by the api
        # If an exception happened while taking the command
        elif 'commandexception' in command:
            self.talk("Sorry, I couldn't hear you")
            self.talk("There might be a problem with your mic")
            self.talk("Please Check that your microphone is working")
            self.handle_command("bye")   # exit the system
        # In case the command wasn't handled
        else:
            self.talk("Sorry, I Can't understand you")


if __name__ == "__main__":
    Marcy = Assistant("hey marcy")
    # Marcy.talk("Hi, I am Marcy, your virtual assistant, how can I help you?")
    #while True:
    #    Marcy.handle_command(Marcy.take_command_text().lower())
    #    Marcy.talk("What else can I help you with?")
