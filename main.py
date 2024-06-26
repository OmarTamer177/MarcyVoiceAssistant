import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia


class Assistant:
    def __init__(self):
        # Initialize the recognizer and TTS engine
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

        # Give marcy a suitable voice
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

    def handle_command(self, command):
        if 'bye' in command:
            self.talk("see you soon bro!")
        elif 'time' in command:
            self.talk("time is right now")
        else:
            self.talk("I Can't understand you")


Marcy = Assistant()

Marcy.talk("Hi, I am Marcy, your virtual assistant, how can I help you?")
Marcy.handle_command(Marcy.take_command())