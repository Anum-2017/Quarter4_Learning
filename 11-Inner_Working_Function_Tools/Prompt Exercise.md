# Step 1: Extract Info from Prompts 

We'll extract the intent and parameters for each prompt.

## 1. "What's the weather going to be like in Dubai tomorrow afternoon?"
- Intent: get_weather_forecast
- Location: "Dubai"
- Datetime: "tomorrow afternoon"

## 2. "Find me some good Chinese restaurants near downtown that are open right now"
- Intent: search_restaurants
- Cuisine: "Chinese"
- Location: "downtown"
- Open now: True

## 3. "Send an email to Sarah about the project deadline being moved to next Wednesday"
- Intent: send_email
- Recipient: "Sarah"
- Subject/Body: "project deadline moved to next Wednesday"

## 4. "Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign"
- Intent: schedule_meeting
= Team: "marketing"
- Datetime: "this Friday at 2 PM"
- Topic: "new campaign"

## 5. "I want to buy a wireless Bluetooth headphones under $100 with good reviews"
- Intent: product_search
- Category: "wireless Bluetooth headphones"
- Budget: < $100
- Sort by: "good reviews"

---

## 📘 What is a Docstring?
A docstring is a special type of string literal used to document a function, class, or module in Python. It is placed just below the definition line and enclosed in triple quotes (""" """ or ''' ''').

## 🧠 Purpose of a Docstring:
- 📄 Describe what the function/class/module does.
- ✅ Clarify the expected input parameters and return values.
- 🧪 Help developers, tools, and LLMs understand the function's purpose without reading the code logic.
- 📚 Automatically used by tools like help(), IDE tooltips, and documentation generators.

# Step 2: Define Functions with Docstrings
Here's a basic simulation using Python functions decorated for use as function_tool.

```python
from agents import function_tool

@function_tool
def get_weather_forecast(location: str, datetime: str) -> str:
    """Returns the weather forecast for the given location and time."""
    return f"Simulated: Weather in {location} on {datetime} will be sunny and 36°C."

@function_tool
def search_restaurants(cuisine: str, location: str, open_now: bool = True) -> list:
    """Searches restaurants by cuisine and location that are currently open."""
    return [f"{cuisine} Place 1", f"{cuisine} Delight 2 near {location}"]

@function_tool
def send_email(to: str, body: str) -> str:
    """Sends an email to the specified recipient with a message body."""
    return f"Email sent to {to}: {body}"

@function_tool
def schedule_meeting(team: str, datetime: str, topic: str) -> str:
    """Schedules a meeting with a team at the specified time and topic."""
    return f"Meeting with {team} team scheduled on {datetime} about '{topic}'."

@function_tool
def product_search(category: str, budget: float, sort_by: str = "reviews") -> list:
    """Searches products under a specified budget and category, sorted by criteria."""
    return [f"{category} Model X - $89", f"{category} Model Y - $79"]
```
