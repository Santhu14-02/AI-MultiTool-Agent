import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


def ask_gemini(messages, retries=3):
    """
    Sends the conversation to Gemini and returns the model's text response.
    Retries automatically on temporary API errors (429, 500, 503).
    """

    prompt = "\n".join(
        f"{m['role'].upper()}: {m['content']}"
        for m in messages
    )

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text.strip()

        except Exception as e:
            error = str(e)

            if (
                "429" in error
                or "503" in error
                or "500" in error
            ) and attempt < retries - 1:
                wait = 5 * (attempt + 1)
                print(f"\n⚠️ Temporary API error. Retrying in {wait} seconds...")
                time.sleep(wait)
                continue

            raise