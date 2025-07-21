# Step 1: Extract Info from Prompts 

We'll extract the intent and parameters for each prompt.

## 1. "What's the weather going to be like in Dubai tomorrow afternoon?"
- Intent: get_weather_forecast
- Location: "Dubai"
- Datetime: "tomorrow afternoon"
- Function needed: get_weather(location, time)

## 2. "Find me some good Chinese restaurants near downtown that are open right now"
- Intent: search_restaurants
- Cuisine: "Chinese"
- Location: "downtown"
- Open now: True
- Function needed: find_restaurants(cuisine, location, open_now)

## 3. "Send an email to Sarah about the project deadline being moved to next Wednesday"
- Intent: send_email
- Recipient: "Sarah"
- Subject/Message: "project deadline moved to next Wednesday"
- Function needed: send_email(to, subject, body)

## 4. "Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign"
- Intent: schedule_meeting
= Team: "marketing"
- Datetime: "this Friday at 2 PM"
- Topic: "new campaign"
- Function needed: schedule_meeting(participants, time, topic)

## 5. "I want to buy a wireless Bluetooth headphones under $100 with good reviews"
- Intent: product_search
- Category: "wireless Bluetooth headphones"
- Budget:  Under $100
- Sort by: "good reviews"
- Function needed: search_products(category, max_price, min_rating)

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
from datetime import datetime

@function_tool
def get_weather(location: str, time: str) -> str:
    """
    Fetches the weather forecast for the given location and time.
    
    Args:
        location (str): City or location.
        time (str): Specific time (e.g., 'tomorrow afternoon').

    Returns:
        str: Weather forecast summary.
    """
    return f"Weather in {location} at {time} is expected to be sunny with a high of 36°C."

@function_tool
def find_restaurants(cuisine: str, location: str, open_now: bool) -> list:
    """
    Finds nearby restaurants based on cuisine and location.

    Args:
        cuisine (str): Type of food.
        location (str): Nearby area or region.
        open_now (bool): Whether to filter by currently open.

    Returns:
        list: List of matching restaurants.
    """
    return [
        {"name": "Golden Dragon", "rating": 4.5},
        {"name": "Wok & Roll", "rating": 4.3}
    ]

@function_tool
def send_email(to: str, subject: str, body: str) -> str:
    """
    Sends an email to a recipient.

    Args:
        to (str): Email address or contact name.
        subject (str): Email subject.
        body (str): Email body.

    Returns:
        str: Confirmation message.
    """
    return f"Email sent to {to} with subject '{subject}'."

@function_tool
def schedule_meeting(participants: str, time: str, topic: str) -> str:
    """
    Schedules a meeting with the specified participants.

    Args:
        participants (str): List or description of attendees.
        time (str): Meeting time.
        topic (str): Meeting agenda.

    Returns:
        str: Meeting confirmation.
    """
    return f"Meeting scheduled with {participants} on {time} about '{topic}'."

@function_tool
def search_products(category: str, max_price: float, min_rating: float = 4.0) -> list:
    """
    Searches products within a category under a budget with good ratings.

    Args:
        category (str): Product category.
        max_price (float): Maximum price.
        min_rating (float): Minimum review rating (default 4.0).

    Returns:
        list: List of recommended products.
    """
    return [
        {"name": "Sony WH-CH520", "price": 79.99, "rating": 4.4},
        {"name": "JBL Tune 510BT", "price": 49.95, "rating": 4.5}
    ]
```

# Step 3: Simulate Agent Running Code
```python
from agents import Agent, Runner

agent = Agent(tools=[get_weather, find_restaurants, send_email, schedule_meeting, search_products])
runner = Runner(agent=agent)

# Simulating running Prompt 1
result = runner.run("What's the weather going to be like in Dubai tomorrow afternoon?")
```

# Step 4: Access Function Tool Response
You can inspect the tool's response like this:

```python
# Get the function tool response
if result.invocations:
    response = result.invocations[0].result
    print("Function_tool response:", response)
```

You’ll get output like:

```
Function_tool response: Weather in Dubai at tomorrow afternoon is expected to be sunny with a high of 36°C.
```
















