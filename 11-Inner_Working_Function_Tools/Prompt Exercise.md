# STEP 1: Prompt Analysis as LLM
We’ll extract intent and key parameters from each prompt.

1. Weather in Dubai tomorrow afternoon
Intent: Get weather forecast

Location: Dubai

Time: Tomorrow afternoon

Tool needed: Weather API

2. Find Chinese restaurants near downtown open now
Intent: Search for restaurants

Cuisine: Chinese

Location: Downtown

Open now: Yes

Tool needed: Google Places / Yelp API

3. Send email to Sarah
Intent: Send an email

Recipient: Sarah

Content: Project deadline moved to next Wednesday

Tool needed: Email client integration (SMTP or Gmail API)

4. Schedule a meeting
Intent: Create calendar event

Participants: Marketing team

Date/Time: This Friday, 2 PM

Topic: New campaign

Tool needed: Google Calendar / Outlook API

5. Buy Bluetooth headphones under $100
Intent: Product search

Category: Wireless Bluetooth headphones

Price Limit: Under $100

Filter: Good reviews

Tool needed: Amazon API / Product API

# STEP 2: Function Implementation with function_tool
Let’s define example functions with function_tool decorators. These can be registered as tools in OpenAI's Agent SDK:

python
Copy
Edit
from agents import function_tool

@function_tool
def get_weather(location: str, datetime: str) -> str:
    """Returns the weather forecast for a given location and time."""
    return f"Weather in {location} on {datetime} is sunny with 38°C."

@function_tool
def find_restaurants(cuisine: str, location: str, open_now: bool = True) -> list:
    """Find restaurants by cuisine and location that are currently open."""
    return [f"{cuisine} Delight", "Wok This Way", "Dragon Express"]

@function_tool
def send_email(to: str, subject: str, body: str) -> str:
    """Sends an email to the recipient with a subject and body."""
    return f"Email sent to {to} with subject '{subject}'"

@function_tool
def schedule_meeting(title: str, datetime: str, participants: list) -> str:
    """Schedules a meeting with participants on a specific date and time."""
    return f"Meeting '{title}' scheduled at {datetime} with {', '.join(participants)}"

@function_tool
def search_products(keyword: str, max_price: float) -> list:
    """Searches for products with good reviews under a specific price."""
    return [f"{keyword} Headset A - $89", f"{keyword} Headset B - $75"]
    
# STEP 3: Run Code & Access function_tool Response
Now suppose we create a mock runner like this:

python
Copy
Edit
from agents import Agent, Runner, RunConfig

agent = Agent(tools=[get_weather, find_restaurants, send_email, schedule_meeting, search_products])

runner = Runner(agent=agent)

result = runner.run("What's the weather going to be like in Dubai tomorrow afternoon?")
Now to access the tool function response, we’d look in:

python
Copy
Edit
function_result = result["steps"][0]["tool_result"]
print("Tool Response:", function_result)
This would return:

python
Copy
Edit
Tool Response: Weather in Dubai on tomorrow afternoon is sunny with 38°C.

# STEP 4: Explore Docstrings
Each function above includes a docstring, used by the agent to understand:

What the function does

What inputs it takes

What output it gives

For example:

python
Copy
Edit
@function_tool
def send_email(to: str, subject: str, body: str) -> str:
    """Sends an email to the recipient with a subject and body."""
This helps the LLM intelligently route user prompts to appropriate tools.
