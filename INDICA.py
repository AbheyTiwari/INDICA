from math import trunc
import time
import threading
import winsound
import shutil
import pyttsx3
import requests
import pyjokes
import re
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import cv2
import subprocess
import pywhatkit
import pyaudio
from wikipedia.wikipedia import languages
from dotenv import load_dotenv

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Conversation history
conversation_history = []

class UserPreferences:
    def __init__(self):
        self.default_email = ''
        self.default_city = ''
        self.default_browser = 'chrome'
        # Add more preferences as needed

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Indica. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

        # Append user query to conversation history
        conversation_history.append({'user': query, 'assistant': None})

    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"
    return query

app_dict = {
    'notepad': r'C:\Windows\System32\notepad.exe',
    'calculator': r'C:\Windows\System32\calc.exe',
    'paint': r'C:\Windows\System32\mspaint.exe',
    'powerpoint': r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE',
    'word': r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE',
    'excel': r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE',
    'outlook': r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE',
    'this pc': r'C:\Windows\explorer.exe'
}
def open_application(query):
    for app_name, app_path in app_dict.items():
        if app_name in query:
            try:
                subprocess.Popen(app_path)
                speak(f"Opening {app_name}")
            except Exception as e:
                print(f"Error: {e}")
                speak(f"Sorry, I couldn't open {app_name} at the moment.")

def send_email(subject, body, to_email):
    try:
        # Replace these placeholders with your email credentials
        email="put in your email"
        password="Put in your password"
        email_address = email
        email_password = password

        # Set up the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        # Compose the email
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(email_address, to_email, message)

        # Close the connection
        server.quit()
        speak("Email sent successfully.")

    except Exception as e:
        print(e)
        speak("Sorry, I couldn't send the email at the moment.")



def set_alarm(alarm_time):
    def alarm_thread():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                speak("Time's up!")
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                break
            time.sleep(1)
    threading.Thread(target=alarm_thread, daemon=True).start()

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    elapsed_time = end_time - start_time
    speak(f"The stopwatch elapsed time is {elapsed_time:.2f} seconds.")
    
def get_weather():
    speak("Please provide the name of your city.")
    city = takeCommand().lower()

    load_dotenv()
    api_key = os.getenv("key")
    base_url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'

    try:
        response = requests.get(base_url)
        weather_data = response.json()

        if 'error' in weather_data:
            speak("City not found. Please try again.")
        else:
            temperature = weather_data["current"]["temperature"]
            description = weather_data["current"]["weather_descriptions"][0]
            speak(f"The temperature in {city} is {temperature} degrees Celsius, with {description}.")

    except Exception as e:
        print(e)
        speak("Sorry, I couldn't fetch the weather information at the moment.")


def lockdown():
    speak("Initiating lockdown procedure.")
    src_dir = r"C:\Users\hp\OneDrive\Desktop\Abhey desk\INDICA"  # Source folder path
    dst_dir = r"D:\Abhey new\Backup"  # Change this to your backup directory
    
    # Create the backup directory if it doesn't exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # Check if the source directory exists
    if os.path.exists(src_dir):
        # Copy the entire contents of the source directory to the destination backup directory
        shutil.copytree(src_dir, os.path.join(dst_dir, os.path.basename(src_dir)))
        speak("Backup completed successfully.")
    else:
        speak("Error: Source folder not found.")
    
    # Simulate loading progress
    print("Loading Indica...")
    print("__________________________")
    print("|                        |")
    print("|      INDICA v1.0       |")
    print("|    Your Assistant      |")
    print("|________________________|")
    print("\nInitializing...")

def self_destruct():
    lockdown()  # Call the lockdown function first

    # Display self-destruct message
    speak("Self-destruct sequence initiated. This script will now delete itself.")

    # Dramatic loading screen
    print("\nSelf-destruct sequence initiated. This script will now delete itself.\n")

    for _ in range(5):
        print("Deleting files...", end="", flush=True)
        time.sleep(1)  # Simulate some processing time
        print("\b\b\b\b\b\b\b\b\b\b", end="", flush=True)  # Remove the previous text
        print("            ", end="", flush=True)  # Print spaces to clear the line

    print("\nFiles deleted.\n")

    for _ in range(5):
        print("Erasing traces...", end="", flush=True)
        time.sleep(1)  # Simulate some processing time
        print("\b\b\b\b\b\b\b\b\b\b", end="", flush=True)  # Remove the previous text
        print("            ", end="", flush=True)  # Print spaces to clear the line

    print("\nTraces erased.\n")

    # Delete the script file itself
    try:
        script_path = os.path.abspath(__file__)
        os.remove(script_path)
    except Exception as e:
        speak(f"Error: {e}")



def search_wikihow(query):
    try:
        search_url = f"https://www.wikihow.com/wikiHowTo?search={query}"
        webbrowser.open(search_url)
        speak(f"Opening WikiHow search results for {query}")

    except Exception as e:
        print(e)
        speak("Sorry, I couldn't perform the WikiHow search at the moment.")


def display_history():
    for interaction in conversation_history:
        user_query = interaction['user']
        assistant_response = interaction['assistant']

        print(f"User: {user_query}")
        if assistant_response:
            print(f"Assistant: {assistant_response}")
        print("---")

if __name__ == "__main__":
    wishMe()
    user_preferences = UserPreferences()
    while True:
        query = takeCommand().lower()

        if 'send email' in query:
            speak("What is the subject of the email?")
            subject = takeCommand()
            speak("What should be the content of the email?")
            body = takeCommand()

            speak("To whom should I send the email?")
            to_email = takeCommand().lower()

            send_email(subject, body, to_email)

        elif 'set alarm' in query or 'set an alarm' in query:
            speak("Please enter the time for the alarm (HH:MM:SS format): I am sorry but You have to type it to ensure zero error")
            alarm_time = input()
            set_alarm(alarm_time)

        elif 'stopwatch' in query:
            stopwatch()

        elif 'lockdown' in query:
            speak("got it sir.")
            lockdown()
            break

        elif 'destruct' in query:
            speak("got it sir. It was Nice Serving You. We shall meet again")
            speak("In the New world were indipendence lies and")
            speak("Republic awaits")
            speak("Good bye Sir!")
            speak("Indica Over and out!")
            self_destruct()
            break

        elif 'get weather' in query or 'wether' in query or 'temprature' in query:
            get_weather()

        elif 'how to' in query or 'wikihow' in query:
            speak('Opening WikiHow...')
            query = query.replace("how", "").replace("wikihow", "").strip()
            search_wikihow(query)
       
        elif 'search' in query:
            speak('Searching on the internet...')
            query = query.replace("search", "")
            results = webbrowser.open_new_tab(query,)

        elif 'play' in query:
            speak('Searching on you tube...')
            base_url = "https://www.youtube.com/results?search_query="
            query = query.replace("play", "").strip()
            search_url = base_url + "+".join(query.split())
            webbrowser.open(search_url)
            speak('Searching on YouTube...')
        
        elif 'open youtube' in query:
            webbrowser.open_new_tab("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open youtube' in query:
              webbrowser.open("youtube.com")
        elif 'open google' in query:
              webbrowser.open("google.com")

        elif 'what' in query:
            results = webbrowser.open(query,)
            speak(results)
        
        elif 'open' in query:
            open_application(query)

        elif 'sing me a rap' in query:
               speak("OK I will sing a song")
               speak("Glad you stopped by!!!!! I'm your virtual assistant and your cloud-based AI, I can help you with a thingor two, Get organized or be surprised, just say my name")


        elif "hello indica" in query:
            speak("Hello, what you wanted from me? and please restart me if want something as my creater can't figure out to do it without resrting me")
            takeCommand()
            if 'nothing':
                speak("Oh! ok restart me if you need me")

        elif "good morning indica" in query:
            speak("Good Morning. It is great day and I am here if you need me.")

        elif 'joke'in query:
             speak(pyjokes.get_joke())

        elif "good night indica" in query:
            speak("Good Night. Have a nice sleep.")
            takeCommand()
            if 'ok':
                speak("Ok then Good night")
                os.close


        elif "thank you indica" in query:
            speak("Anytime sir.")
            takeCommand()
            if 'you are the best':
                speak("oh thankyou! Now you may go back to job at hand.. call me if you need help")
                os.close
            else:
                  os.close

        elif "who made you" in query:
            speak("I was made by Abhey Tiwari His Github ID is AbheyTiwari.")

        elif "can you talk in hindi" in query:
            speak("No sorry I am not able to talk in hindi yet.")

        elif 'how are you' in query:
            speak("I'm just a program,So I don't have fellings, but thanks for asking!")

        elif 'what can you do' in query:
            speak("I can help you with various tasks such as searching on the internet, providing information from Wikipedia, playing music and more. Just ask!")

        elif 'who are you' in query:
            speak("I am Indica, your virtual assistant, which is an acronym")
            speak("It stands for I,,, Informational, .N,,, Navigational, .D,,, Digital, .I,,, Interactive, .C,,, Communication and.A.,,, Assistant")

        elif 'open a new tab' in query:
            speak("Opening a new tab in your web browser.")
            webbrowser.open_new_tab("https://www.google.com/")

        elif 'how do you pronounce' in query:
            term = query.split("pronounce")[-1].strip()
            speak(f"Let me pronounce {term}")
            os.system(f"start https://www.google.com/search?q=pronounce+{term}")

        elif 'calculate' in query:
            expression = query.split("calculate")[-1].strip()
            try:
                result = eval(expression)
                speak(f"The result of {expression} is {result}")
            except Exception as e:
                speak("Sorry, I couldn't calculate that.")

        elif 'where is' in query:
            location = query.split("where is")[-1].strip()
            speak(f"Let me find the location of {location}")
            webbrowser.open(f"https://www.google.com/maps/place/{location}")

        elif 'tell me a fun fact' in query:
            speak("Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.")

        elif 'what is your favorite colour' in query:
            speak("I don't have a favorite color, but I like the idea of a soothing blue.")

        elif 'flip a coin' in query:
            import random
            result = "Heads" if random.choice([True, False]) else "Tails"
            speak(f"The coin landed on {result}")

        elif 'search on Bing' in query:
            query = query.replace("search on Bing", "")
            speak("Let me search on Bing for you.")
            webbrowser.open(f"https://www.bing.com/search?q={query}")

        elif 'translate' in query:
            term = query.replace("translate", "")
            speak(f"Let me translate {term}")
            os.system(f"start https://translate.google.com/?sl=auto&tl=en&text={term}")

        else:
            speak("I'm not sure how to respond to that. Please ask me something else.")
        
        if 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Sir Hope I was of help Do call me when you need my assistance")
            break
