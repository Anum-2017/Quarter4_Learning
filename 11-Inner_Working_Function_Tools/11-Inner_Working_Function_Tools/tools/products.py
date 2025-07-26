# def search_products(query: str, max_price: float, sort_by: str = "reviews") -> list:
#     """
#     Searches for products matching the given criteria.

#     Parameters:
#     - query (str): Search keyword (e.g., 'Bluetooth headphones').
#     - max_price (float): Maximum price.
#     - sort_by (str): Sort criteria, like 'reviews' or 'price'.

#     Returns:
#     - list: List of product names with prices and ratings.
#     """
#     return [
#         f"{query} - $79.99 - ★★★★☆",
#         f"{query} - $59.49 - ★★★★☆"
#     ]

def search_products(category: str, max_price: float, min_rating: float = 0.0) -> list:
    """
    Searches for products.

    Parameters:
    - category (str): Product type or keyword
    - max_price (float): Maximum price
    - min_rating (float): Minimum acceptable rating

    Returns:
    - list: Product list
    """
    return [
        f"{category} - $79.99 - ★★★★☆",
        f"{category} - $59.49 - ★★★★☆"
    ]

