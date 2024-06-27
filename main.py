import sys
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit as pwk
import wikipedia as wiki


class Assistant:
    def __init__(self):
        # Initialize the Speech Recognizer and Text To Speech engines
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

        # Give Marcy a suitable voice
        voices = self.tts_engine.getProperty('voices')
        self.tts_engine.setProperty('voice', voices[1].id)

    # Function to convert text to speech
    def talk(self, text):
        print(text)
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    # Function to take voice input
    def take_command(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)
                command = command.lower()
        except Exception as e:
            print(e)
            return ""
        return command

    # Function to take text input (for testing purpose)
    def take_command_text(self):
        command = input("Me: ")
        return command

    # Function to handle the commands
    def handle_command(self, command):
        # Exit the app
        if 'bye' in command or 'quit' in command or 'exit' in command:
            self.talk("see you soon!")
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
        # In case the command wasn't handled
        else:
            self.talk("Sorry, I Can't understand you")


if __name__ == "__main__":
    Marcy = Assistant()
    Marcy.talk("Hi, I am Marcy, your virtual assistant, how can I help you?")
    while True:
        Marcy.handle_command(Marcy.take_command_text().lower())
        Marcy.talk("What else can I help you with?")
