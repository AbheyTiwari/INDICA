# ai_engine/gemini_research.py

import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
import json
import re

def extract_research_json(text):
    """
    Cleans Gemini output and extracts fields relevant to research.
    """
    cleaned = re.sub(r"```(?:json)?", "", text).replace("```", "").strip()

    try:
        parsed = json.loads(cleaned)
        return {
            "should_search": parsed.get("should_search", False),
            "summary": parsed.get("summary", "No summary provided."),
            "filename": parsed.get("filename", "research_output.txt"),
            "raw_text": parsed.get("raw_text", ""),
            "links": parsed.get("links", [])
        }
    except json.JSONDecodeError:
        return {
            "should_search": False,
            "summary": "Gemini could not parse the result.",
            "filename": "invalid_response.txt",
            "raw_text": text,
            "links": []
        }

def run_gemini_research(query):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)

        prompt = f"""
You are INDICA's smart research agent.

The user has asked: "{query}"

Your goal:
1. Give a deep but readable summary of the topic using your knowledge.
2. If the topic needs external sources (gov data, news), include a field 'should_search': true.
3. Suggest a filename like: "forest_fire_impact_india.txt".
4. Include a 'summary' and a 'raw_text' version.
5. In 'links', only list URLs if 'should_search' is true.

Format:
{{
  "should_search": true/false,
  "summary": "...",
  "filename": "...",
  "raw_text": "...",
  "links": ["https://...", "https://..."]
}}

NO markdown. NO extra commentary. Plain JSON only.
"""
        response = model.generate_content(prompt)
        return extract_research_json(response.text.strip())

    except Exception as e:
        return {
            "should_search": False,
            "summary": f"Gemini error: {e}",
            "filename": "gemini_error.txt",
            "raw_text": "",
            "links": []
        }
