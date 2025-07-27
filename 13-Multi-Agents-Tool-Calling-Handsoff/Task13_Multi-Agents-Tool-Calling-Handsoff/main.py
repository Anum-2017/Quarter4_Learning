import os
import requests
from dotenv import load_dotenv
import rich
from agents import Agent, Runner, function_tool
from connection import config

@function_tool
def current_location() -> str:
    """Returns current location using public IP info."""
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get("city", "Unknown City")
        country = data.get("country", "Unknown Country")
        return f"📍 Your current location is: {city}, {country}."
    except Exception as e:
        return f"⚠️ Could not fetch location. Error: {str(e)}"

@function_tool
def breaking_news() -> str:
    """Returns a mock breaking news update."""
    return "📰 Breaking News: AI agents are revolutionizing education and software development!"

# Define agents
plant_agent = Agent(
    name="Plant Agent",
    instructions="You are a plant biology expert. Answer questions related to plants like photosynthesis."
)

main_agent = Agent(
    name="Main Agent",
    instructions="You are a helpful assistant. Use tools for general questions and hand off plant-related ones to the Plant Agent.",
    tools=[current_location, breaking_news],
    handoffs=[plant_agent]
)

# Query
query = """
1. What is my current location?
2. Any breaking news?
3. What is photosynthesis?
"""

# Run agent
result = Runner.run_sync(
    main_agent,
    query,
    run_config=config
)

# Output
print("Last Agent Used:", result.last_agent.name if result.last_agent else "Unknown")
# print("=" * 50)
# print("Answer Parts:")
for item in result.new_items:
    rich.print(item)
print("=" * 50)
print("Final Output:")
rich.print(result.final_output)



