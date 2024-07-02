import sys
import speech_recognition as sr
import pyttsx3
from functions import *


def get_after(command, word):
    index = command.split().index(word) + 1
    after = ""
    for i in command.split()[index:]:
        after += i
        if i != command.split()[len(command.split()) - 1]:
            after += " "
    return after


class Assistant:
    def __init__(self, name):
        # Initialize the Speech Recognizer and Text To Speech engines
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

        # Give Marcy a suitable voice
        voices = self.tts_engine.getProperty('voices')
        self.tts_engine.setProperty('voice', voices[1].id)

        # Wake word
        self.name = name

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
            self.talk("time is " + get_time())

        # Getting today's date
        elif 'date' in command:
            self.talk("today is " + get_date())

        # Getting a random joke
        elif 'joke' in command:
            joke = get_joke()
            self.talk("I have a good joke for you!")
            self.talk(joke + "\nha ha ha ha!!")

        elif 'wikipedia' in command or 'summary' in command or 'know about' in command or 'tell me about' in command:
            topic = get_after(command, "about")
            summary = get_summary(topic)
            self.talk(summary[0])

        elif 'whatsapp' in command or 'message' in command:
            self.talk("who do you want to message?")
            contact = self.take_command_text()
            self.talk("what do you want to say?")
            msg = self.take_command_text()
            send_msg(contact, msg)
            self.talk("message sent!")

        elif 'google' in command:
            if 'search' in command:
                topic = get_after(command, "search")
            else:
                topic = get_after(command, "google")
            google_search(topic)

        elif 'youtube' in command or 'video' in command:
            if 'about' in command:
                topic = get_after(command, "about")
            elif 'video' in command:
                topic = get_after(command, "video")
            else:
                topic = get_after(command, "youtube")
            open_yt_video(topic)

        elif 'screenshot' in command:
            take_screenshot()

        elif 'weather' in command:
            self.talk("Which city do you want to know about?")
            city = self.take_command_text()
            temp, humidity, pressure, wind = get_weather(city)
            self.talk("In " + city + " temperature is " + str(int(temp)) + " degrees C")
            self.talk("humidity is " + str(humidity) + "%")
            self.talk("pressure is " + str(pressure) + " hecto pascals")
            self.talk("wind speed is " + str(wind) + " miles per hour")

        elif 'program' in command or 'open' in command:
            program = get_after(command, "open")
            open_program(program)

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
    Marcy = Assistant("marcy")
    Marcy.talk("Hi, I am Marcy, your virtual assistant, how can I help you?")
    while True:
        Marcy.handle_command(Marcy.take_command_text().lower())
        Marcy.talk("What else can I help you with?")
