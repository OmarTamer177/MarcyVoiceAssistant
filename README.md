# Marcy

Marcy is a virtual assistant developed using Python. It can handle various tasks such as fetching weather information, performing Google searches, opening YouTube videos, and even sending WhatsApp messages. Marcy listens for voice commands and responds with voice output, making it a versatile and interactive assistant.

## Features

- **Time and Date**: Provides the current time and date.
- **Weather Information**: Fetches and reports weather details for a specified city.
- **Wikipedia Summary**: Retrieves and summarizes information from Wikipedia.
- **Google Search**: Performs Google searches based on user queries.
- **YouTube Video**: Opens YouTube videos based on the given topic.
- **Application Launcher**: Opens specified applications installed on the system.
- **WhatsApp Messaging**: Sends WhatsApp messages to contacts.

## Technologies Used

- **Python**
- **SpeechRecognition**: For converting speech input into text.
- **Pyttsx3**: For text-to-speech conversion.
- **Pywhatkit**: For various utilities like Google searches, playing YouTube videos, and sending WhatsApp messages.
- **WikipediaAPI**: For fetching summaries from Wikipedia.
- **Requests**: For making API calls, such as fetching weather data.
- **OpenWeatherMap API**: For retrieving current weather information.
- **Datetime**: For fetching the current date and time.
- **OS**: For opening applications installed on the system.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/marcy-virtual-assistant.git
   cd marcy-virtual-assistant

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Create and Activate a Virtual Environment**

   Create a .env file in the root directory and add your OpenWeatherMap API key:
   ```bash
   WEATHER_API_KEY=your_api_key_here
   
6. **Run Virtual Assistant**
   ```bash
   python main.py
