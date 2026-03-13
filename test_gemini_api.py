import asyncio
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_FULL_NAME = "models/gemini-1.5-flash"
BASE_URL = f"https://generativelanguage.googleapis.com/v1beta/{MODEL_FULL_NAME}:generateContent"

async def test_gemini():
    if not GEMINI_API_KEY:
        print("GEMINI_API_KEY not found")
        return

    url = f"{BASE_URL}?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": "Hello, who are you?"}]}]
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, timeout=15)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_gemini())
