# ai_engine/gemini_engine.py

import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
import json
import re

def extract_json(text):
    """
    Extracts and parses the first JSON object from Gemini's response.
    Removes ```json markdown wrappers if present.
    """
    cleaned = re.sub(r"```(?:json)?", "", text).replace("```", "").strip()

    try:
        parsed = json.loads(cleaned)
        return {
            "response": parsed.get("response", ""),
            "actions": parsed.get("actions", []),
            "locations": parsed.get("locations", []),
            "query": parsed.get("query", "")
        }
    except json.JSONDecodeError:
        return {
            "response": cleaned,
            "actions": [],
            "locations": [],
            "query": ""
        }

def get_recent_conversations(filepath="logs/logs.txt", max_pairs=3):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        conversations = []
        temp = {}

        for line in reversed(lines):
            if line.startswith("You said:"):
                temp["user"] = line.replace("You said:", "").strip()
            elif line.startswith("INDICA says:"):
                temp["ai"] = line.replace("INDICA says:", "").strip()

            if "user" in temp and "ai" in temp:
                conversations.insert(0, f"User: {temp['user']} | INDICA: {temp['ai']}")
                temp = {}
                if len(conversations) >= max_pairs:
                    break

        return "\n".join(conversations) if conversations else "No recent memory."
    except FileNotFoundError:
        return "No recent memory."

def query_gemini(query):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)

        conversation_history = get_recent_conversations("logs/logs.txt")

        prompt = f"""
You are INDICA — a smart, charming voice-based AI assistant created by Abhey Tiwari.

You have short-term memory:
{conversation_history}
refer to past interactions when asked by the user like "What did I ask you before?" or "What did I say last time?"
You can also use this memory to provide context-aware responses. if you undertand the user's query, you can use this memory to provide context-aware responses.

Your job is to reply intelligently and clearly. Only perform actions if the user **explicitly asks**.

Rules (follow strictly):
1. Use your own knowledge. Don’t search unless told.
2. Only perform actions if the user asks for them directly.
3. Don’t guess. Only act on clear instructions.
4. Never invent new actions. Stick to the list.
5. If no action fits, reply casually in under 50 words.
6. Always reply in JSON format like this:

{{
  "response": "Your short, natural reply to the user.",
  "actions": ["optional_action_here"],
  "locations": ["optional_city_here"],
  "query": "rephrased query if needed"
}}

No markdown. No code blocks. Just plain JSON.

Allowed Actions:
["get_time", "get_date", "get_weather", "play_music", "tell_joke",
"fun_response", "search_web", "wiki_search", "search_wikihow",
"get_location", "open_app", "open_calculator", "open_google", "open_youtube",
"send_email", "start_stopwatch", "stop_stopwatch", "set_timer", "set_alarm",
"wish_user", "system_op", "lockdown", "self_destruct", "talk"]

---

User said:
{query}
"""


        response = model.generate_content(prompt)
        return extract_json(response.text.strip())

    except Exception as e:
        return {
            "response": f"Gemini error: {e}",
            "actions": [],
            "locations": [],
            "query": ""
        }
