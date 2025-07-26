# def send_email(to: str, subject: str, content: str) -> str:
#     """
#     Simulates sending an email.

#     Parameters:
#     - to (str): Recipient's name or email.
#     - subject (str): Subject of the email.
#     - content (str): Body/content of the email.

#     Returns:
#     - str: Confirmation message.
#     """
#     return f"Email successfully sent to {to} with subject '{subject}' and content: '{content}'"

def send_email(to: str, subject: str, body: str) -> str:
    """
    Sends an email.

    Parameters:
    - to (str): Recipient
    - subject (str): Subject line
    - body (str): Body/content of the email

    Returns:
    - str: Confirmation message.
    """
    return f"Email successfully sent to {to} with subject '{subject}' and body: '{body}'"
