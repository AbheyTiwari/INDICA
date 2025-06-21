INDICA v1.0
Intelligent Natural Dialogue Interface & Cognitive Assistant
A Mango-rooted AI with purpose, power, and memory.

🌟 What is INDICA?
INDICA is a terminal-based virtual assistant developed by Abhey Tiwari. Originally inspired by a love for mangoes (Mangifera indica), the name later gained depth — also referencing the ancient Indian text Indica by Megasthenes.

Built using Python and powered by the Gemini API, INDICA merges voice interaction, smart task automation, and short-term memory, making it feel like a responsive and intelligent digital companion — all without the fluff of a flashy UI.

🚀 Features
💬 Voice Interaction
Execute tasks with natural spoken commands

Powered by speech_recognition + pyttsx3 for text-to-speech

🔐 Gemini-Powered AI Brain
Structured prompting with behavior rules

Action-limited responses to avoid hallucinations

Feels like a true assistant, not a chatbot

🧠 Short-Term Memory
Stores the last 5 interactions in logs/logs.txt

Injected into Gemini context for continuity and recall

🛠️ Action-Based Task Handling
Supports powerful command categories:

📧 Email Sending – Secure SMTP-based mailer

⏰ Alarm & Stopwatch – Set alarms and run stopwatches

🌤️ Weather Information – Real-time weather from APIs

🖥️ App Launcher – Opens local apps with your voice

🔍 Web Search – Search YouTube, Google, WikiHow

🤖 Fun Utilities – Tells jokes, facts, plays music

🔒 System Commands – Lock, shutdown, and self-destruct modes

🛡️ Guardrails and Safety
No unauthorized actions

Explicit command-only mode

Jokes/fun facts only when asked

📂 Project Structure
bash
Copy
Edit
INDICA/
├── ai_engine/
│   └── gemini_engine.py       # Gemini API interface
├── logs/
│   └── logs.txt               # Short-term memory
├── utils/
│   ├── tts.py                 # Text-to-speech module
│   ├── voice_input.py         # Voice command recognizer
│   └── actions.py             # Executable command actions
├── config.py                  # API keys, voice config, and settings
├── main.py                    # INDICA runtime (terminal-based)
└── app.py (optional)          # Flask wrapper (if used)
🔧 Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/indica.git
cd indica
2. Create a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set Environment Variables
Create a .env file in the root:

env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key
WEATHERSTACK_API_KEY=your_weather_api_key
🧪 Usage
Run the assistant:

bash
Copy
Edit
python main.py
It will greet you and begin listening. Speak clearly to issue commands.

Example Commands:

"What's the weather in Delhi?"

"Send an email to Riya"

"Open YouTube"

"Tell me a joke"

"Start a stopwatch"

"Lock the system"

🧠 Dependencies
INDICA uses the following Python libraries:

pyttsx3, speech_recognition, pyaudio

datetime, threading, os, re

requests, pyjokes, webbrowser, wikipedia

cv2, pywhatkit, subprocess, smtplib

dotenv, time, math, shutil

🤝 Contributing
Feel free to fork this repo, experiment, and make INDICA even smarter.

For major feature changes or ideas, open an issue first for discussion.

🎯 Future Scope
Long-Term Memory integration

GUI version (Flask or Electron)

Face & voice-based user recognition

Secure remote commands

Plugin system for custom user actions

Crafted with ❤️ and mangoes by Abhey Tiwari
Your world, voice-controlled.
