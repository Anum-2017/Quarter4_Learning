def get_weather(location: str, time: str = "now") -> str:
    """
    Fetches the weather forecast for a given location and time.

    Parameters:
    - location (str): Name of the city or location.
    - time (str): Time reference like 'now', 'tomorrow afternoon', etc.

    Returns:
    - str: A simulated weather forecast.
    """
    return f"The weather in {location} at {time} is expected to be sunny with temperatures around 30°C."
