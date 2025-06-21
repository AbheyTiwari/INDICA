# dispatcher.py

from modules.time import get_time as say_time
from modules.weather import get_weather
from modules.music import play_music
from modules.search import search_web
from modules.wiki import search_wikipedia
from modules.location import locate_place
from modules.fun import tell_joke, sing_rap
from modules.clock import start_stopwatch, stop_stopwatch, set_timer, set_alarm
from modules.apps import open_application
from modules.sytem import perform_system_op
from modules.wish import wish_me
from modules.email import send_email
from tts import speak
from datetime import datetime
now = datetime.now().strftime("%A, %B %d, %Y")
import subprocess
import webbrowser
import pyjokes

def dispatch(actions: list, context: dict):
    """
    Executes actions returned from Gemini with context information.
    """

    for action in actions:
        match action:

            # 🎯 Time & Date
            case "get_time":
                say_time()

            case "get_date":
                now = datetime.now().strftime("%A, %B %d, %Y")
                speak(f"Today is {now}")

            # ⏰ Clock Utilities
            case "start_stopwatch":
                start_stopwatch()

            case "stop_stopwatch":
                stop_stopwatch()

            case "set_timer":
                query = context.get("query", "")
                try:
                    seconds = int(''.join(filter(str.isdigit, query)))
                    set_timer(seconds)
                except:
                    speak("Could not set timer. Please specify duration.")

            case "set_alarm":
                query = context.get("query", "")
                set_alarm(query)

            # ☁️ Weather
            case "get_weather":
                locations = context.get("locations", [])
                if locations:
                    for city in locations:
                        get_weather(city)
                else:
                    get_weather()  # Default city

            # 🎵 Entertainment
            case "play_music":
                query = context.get("query", "")
                if query:
                    play_music(query)
                else:
                    speak("Please tell me what song or genre you'd like.")

            case "tell_joke":
                tell_joke()

            case "fun_response":
                query = context.get("query", "").lower()
                if "joke" in query:
                    tell_joke()
                elif "rap" in query or "song" in query:
                    sing_rap()
                else:
                    speak("Would you like a joke or a song?")

            # 🔍 Search
            case "search_web":
                query = context.get("query", "")
                search_web(query)

            case "wiki_search":
                query = context.get("query", "")
                search_wikipedia(query)

            case "search_wikihow":
                webbrowser.open("https://www.wikihow.com/Main-Page")
                speak("Opening WikiHow.")

            case "get_location":
                places = context.get("locations", [])
                for place in places:
                    locate_place(place)

            # 🌐 Apps & Web
            case "open_app":
                query = context.get("query", "")
                open_application(query)

            case "open_calculator":
                subprocess.Popen("calc.exe")
                speak("Opening Calculator.")

            case "open_google":
                webbrowser.open("https://www.google.com")
                speak("Opening Google.")

            case "open_youtube":
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube.")

            # 📧 Email
            case "send_email":
                speak("Email feature is still under setup. Will be available soon.")

            # 🖥️ System Ops
            case "system_op":
                command = context.get("query", "")
                perform_system_op(command)

            # 👋 Greeting
            case "wish_user":
                wish_me()

            # 🔒 Secure Ops
            case "lockdown":
                speak("Lockdown feature not configured yet.")

            case "self_destruct":
                speak("Self-destruction is not allowed for now. 😅")

            # ❓ Unknown
            case _:
                speak(f"Sorry, I don't know how to perform '{action}' yet.")
