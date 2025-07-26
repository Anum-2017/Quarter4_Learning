import os
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

from tools.weather import get_weather
from tools.restaurant import find_restaurants
from tools.email import send_email
from tools.schedule import schedule_meeting
from tools.products import search_products


prompts = [
    "What's the weather going to be like in Dubai tomorrow afternoon?",
    "Find me some good Chinese restaurants near downtown that are open right now",
    "Send an email to Sarah about the project deadline being moved to next Wednesday",
    "Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign",
    "I want to buy a wireless Bluetooth headphones under $100 with good reviews"
]


# === Gemini Tool Router ===
def call_tool(prompt: str) -> str:
    tools_used = {
        "get_weather": get_weather,
        "find_restaurants": find_restaurants,
        "send_email": send_email,
        "schedule_meeting": schedule_meeting,
        "search_products": search_products
    }

    # 🧠 Correct instruction block (matches your actual function signatures)
    instruction = f"""
You are a function router. Given a prompt: "{prompt}", decide:
1. Which function to use from: get_weather, find_restaurants, send_email, schedule_meeting, search_products
2. What arguments to pass.

Use exact argument names from these function definitions:
- get_weather(location: str, time: str)
- find_restaurants(cuisine: str = None, location: str = None, open_now: bool = True)
- send_email(to: str, subject: str, body: str)
- schedule_meeting(participants: str, time: str, topic: str)
- search_products(category: str, max_price: float, min_rating: float = 4.0)

✅ Return ONLY a valid single-line Python function call like:
schedule_meeting(participants="marketing team", time="Friday 2 PM", topic="New campaign")

❌ Do NOT return explanations or markdown code blocks like ```python.
"""

    response = model.generate_content(instruction)
    generated_code = response.text.strip()

    # 🧼 Sanitize output (remove any ``` or stray text)
    generated_code = re.sub(r"^```(?:python)?|```$", "", generated_code, flags=re.MULTILINE).strip()
    generated_code = generated_code.splitlines()[-1]

    print(f"🔎 Gemini Suggestion: {generated_code}")

    try:
        result = eval(generated_code, globals(), tools_used)
        return result
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
     for prompt in prompts:
        print(f"\n🟢 Prompt: {prompt}")
        response = call_tool(prompt)
        print(f"✅ Response: {response}")



