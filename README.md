<h1 align="center">
  🤖 INDICA v1.0  
  <br>
  <sub><i>Intelligent Natural Dialogue Interface & Cognitive Assistant</i></sub>
</h1>

<p align="center">
  <b>A mango-rooted AI with purpose, power, and memory 🍋</b>
  <br>
  <i>Created by <a href="https://github.com/AbheyTiwari">Abhey Tiwari</a></i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Gemini-API-green?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Voice-Controlled-Yes-purple?style=for-the-badge&logo=voicemod" />
</p>

---

## 🌟 What is INDICA?

> INDICA is your voice-powered virtual assistant that **thinks, talks, and acts** — combining Gemini AI, command execution, and memory into one smooth Python experience.

Originally named after the creator’s love for mangoes (*Mangifera indica* 🥭), **INDICA** now stands for:

> **I**ntelligent **N**atural **D**ialogue **I**nterface & **C**ognitive **A**ssistant  

It also pays homage to *Indica*, the legendary text by Megasthenes 🇮🇳📜.

---

## ✨ Features

### 🧠 Memory System
- Stores **last 5 conversations** in `logs/logs.txt`
- Injects memory context into Gemini prompts for continuity
- Long-Term Memory support (Coming soon)

### 💬 Voice Interaction
- Talk naturally using speech recognition 🎤
- Responses are **spoken out loud** with `pyttsx3` 🗣️
- Can be extended to multi-user recognition

### ⚙️ Smart Action System
- Gemini-driven **action parsing**
- Supports:
  - `open_app`, `send_email`, `get_weather`, `play_music`, etc.
- Actions dispatched only when explicitly requested

### 🔐 Sanity & Safety
- No hallucinated actions
- No implicit commands
- No "guessing" behavior
- Only performs what it is **clearly instructed to do**

---

## 🧱 Project Structure

```mermaid
flowchart TD
    %% Style definitions
    classDef user fill:#cce5ff,stroke:#003366,stroke-width:2px;
    classDef speech fill:#d4edda,stroke:#155724,stroke-width:2px;
    classDef parser fill:#fff3cd,stroke:#856404,stroke-width:2px;
    classDef decision fill:#f8d7da,stroke:#721c24,stroke-width:2px;
    classDef rag fill:#e2e3e5,stroke:#383d41,stroke-width:2px;
    classDef sys fill:#f1e0ff,stroke:#5a005a,stroke-width:2px;
    classDef tts fill:#d1ecf1,stroke:#0c5460,stroke-width:2px;
    classDef memory fill:#fefefe,stroke:#343a40,stroke-width:2px,stroke-dasharray:5 5;

    %% User
    User(["👤 <b>User</b><br/>(Voice Command)"]):::user

    %% Speech to text
    STT(["🗣️ <b>Speech-to-Text</b><br/>(Whisper etc.)"]):::speech

    %% Parser
    Parser(["🧩 <b>Intent Recognizer</b><br/>(Command Parser)"]):::parser

    %% Decision Engine
    Decision(["⚙️ <b>Decision Engine</b><br/>(Task Router)"]):::decision

    %% Tasks
    RAG(["🧠 <b>Retrieval-Augmented Generator</b><br/>(LLM + Context)"]):::rag
    SysCtrl(["🖥️ <b>System Control</b><br/>(Shutdown, Open Apps)"]):::sys

    %% TTS
    TTS(["🔊 <b>Text-to-Speech</b><br/>(Voice Out)"]):::tts

    %% Memory
    subgraph Memory["🗂️ <b>Memory</b>"]
        ShortTerm(["⏳ <b>Short-Term Memory</b><br/>(Current Session)"]):::memory
        LongTerm(["🗃️ <b>Long-Term Memory</b><br/>(Logs + Embeddings)"]):::memory
    end

    %% Flows
    User -->|Voice| STT
    STT -->|Text| Parser
    Parser -->|Intent| Decision
    Decision -->|Knowledge Task| RAG
    Decision -->|System Task| SysCtrl
    RAG -->|Answer| TTS
    SysCtrl -->|Confirmation| TTS
    TTS -->|Voice| User

    %% Memory connections
    Parser --> Memory
    RAG --> Memory
    SysCtrl --> Memory

    %% Note
    note over Decision
        Single Agent Architecture<br/>Voice-driven, Retrieval-Augmented
    end

```


```bash
INDICA/
├── ai_engine/
│   └── gemini_engine.py     # Gemini LLM logic
├── modules/
│   ├── wish.py              # Greets the user
│   ├── memory.py            # Memory handling
│   └── ...                  # Extendable modules
├── logs/
│   └── logs.txt             # Short-term memory
├── dispatcher.py            # Action dispatch engine
├── listener.py              # Voice input
├── tts.py                   # Voice output (text-to-speech)
├── config.py                # API keys & settings
└── main.py                  # Entry point to run INDICA
🔧 Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/AbheyTiwari/indica.git
cd indica
(Optional) Create a Virtual Environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure API Keys:

Create a .env file and add:

env
Copy
Edit
GEMINI_API_KEY=your_google_gemini_key
WEATHERSTACK_API_KEY=your_weather_api_key
🚀 Usage
Just run the main file:

bash
Copy
Edit
python main.py
Now speak naturally. INDICA will reply and take action when applicable.

🗣️ Sample Commands:
"What time is it?"

"Send an email to Rahul"

"Open Spotify"

"Get weather in Delhi"

"Tell me a joke"

"Search Python on Wikipedia"

🧰 Dependencies
Includes support for:

lua
Copy
Edit
pyttsx3, speech_recognition, python-dotenv,
requests, pywhatkit, wikipedia, pyjokes,
datetime, subprocess, smtplib, webbrowser,
cv2, os, threading, winsound, re
🛠️ Contributing
Got an idea to make INDICA even better?

Fork the repo 🍴

Create a new branch 🎋

Commit your changes ✍️

Open a pull request 🚀

