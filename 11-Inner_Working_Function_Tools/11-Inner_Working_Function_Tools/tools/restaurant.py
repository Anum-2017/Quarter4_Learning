def find_restaurants(cuisine: str, location: str, open_now: bool = True) -> list:
    """
    Finds restaurants based on cuisine, location, and open status.

    Parameters:
    - cuisine (str): Type of food (e.g., 'Chinese').
    - location (str): Area or city (e.g., 'downtown').
    - open_now (bool): Whether the restaurant should be open now.

    Returns:
    - list: A list of restaurant names.
    """
    return [
        f"{cuisine} Palace - {location} (Open Now)",
        f"{cuisine} Bistro - {location} (Open Now)"
    ]
