import google.generativeai as genai

from config import GEMINI_API_KEY, MAX_OUTPUT_TOKENS, TEMPERATURE

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-001",
    generation_config={
        "temperature": TEMPERATURE,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
    },
)
