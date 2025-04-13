"""
Configuration settings for the Gemini API wrapper
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please set it in your .env file or environment variables."
    )

# Gemini API settings
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
TEMPERATURE = 0.7
MAX_OUTPUT_TOKENS = 1024
TOP_P = 0.95
TOP_K = 40
