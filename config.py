# config.py

# ===== API KEYS =====
GEMINI_API_KEY = "PUT YOUR GEMINI API_KEY HERE"  # Replace if needed
WEATHERSTACK_API_KEY = "PUT YOUR WEAHERSTACK API_KEY HERE"

# ===== DEFAULT USER PREFERENCES =====
DEFAULT_CITY = "PUT YOUR DEFUALT CITY"
DEFAULT_BROWSER = "chrome"
DEFAULT_EMAIL = ""  # Add your email if needed
EMAIL_PASSWORD = ""  # Caution: Load from .env or vault later

# ===== LOGGING =====
CONVERSATION_LOG_PATH = "logs/logs.txt"

# ===== VOICE SETTINGS =====
VOICE_INDEX = 1  # 0 for male, 1 for female (depends on system)
SPEECH_RATE = 180  # Optional: control speed

# ===== GEMINI SETTINGS =====
MAX_RESPONSE_WORDS = 50
GEMINI_MODEL = "gemini-2.0-flash"  # Use "pro" for slower, more thoughtful responses
