import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("1. API key loaded:", bool(api_key))

try:
    client = genai.Client(api_key=api_key)

    print("2. Gemini client created")
    print("3. Sending request...")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Reply with exactly: Gemini connection works."
    )

    print("4. Request completed")
    print("5. Response:")
    print(response.text)

except Exception as e:
    print("\n===== GEMINI ERROR =====")
    print("Error type:", type(e).__name__)
    print("Error:", e)