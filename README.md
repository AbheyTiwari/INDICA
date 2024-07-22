# INDICA - Your Virtual Assistant

INDICA (Informational Navigational Digital Interactive Communication Assistant) is a Python-based virtual assistant capable of performing various tasks like opening applications, sending emails, setting alarms, fetching weather information, and more.

## Features

- **Voice Interaction**: Communicates with the user through voice commands.
- **Email Sending**: Sends emails using voice commands.
- **Weather Information**: Fetches and provides weather details for any city.
- **Alarm Setting**: Allows setting alarms.
- **Application Launcher**: Opens various applications on your system.
- **Jokes and Fun Facts**: Tells jokes and interesting facts.
- **Web Searches**: Performs searches on the internet, YouTube, WikiHow, etc.
- **System Lockdown and Self-Destruct**: Includes a lockdown and self-destruct sequence.
- **Stopwatch**: Simple stopwatch functionality.
- **Command History**: Maintains a history of user interactions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/indica.git
   cd indica
2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:
   pip install -r requirements.txt
   
4. Set up your environment variables:
Create a .env file in the root directory.
Add your API key for weather information:
key=your_weather_api_key

#Usage
Run the script:
python indica.py
The assistant will greet you and ask for your command. Use voice commands to interact with INDICA. Some example commands include:

"Send email"
"Set an alarm"
"Get weather"
"Open YouTube"
"Tell me a joke"
"Search on the internet"
Dependencies
The project requires the following Python libraries:

math
time
threading
winsound
shutil
pyttsx3
requests
pyjokes
re
wikipedia
speech_recognition
datetime
webbrowser
os
smtplib
cv2
subprocess
pywhatkit
pyaudio
python-dotenv
Contribution
Feel free to fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
