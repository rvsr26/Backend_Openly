import asyncio
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def list_models():
    if not GEMINI_API_KEY:
        print("GEMINI_API_KEY not found")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=15)
            data = response.json()
            if "models" in data:
                for m in data["models"]:
                    print(f"- {m['name']} ({m.get('displayName', 'N/A')})")
            else:
                print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(list_models())
