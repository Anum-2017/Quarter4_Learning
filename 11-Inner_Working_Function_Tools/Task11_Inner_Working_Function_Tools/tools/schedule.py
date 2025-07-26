# def schedule_meeting(participants: str, datetime: str, topic: str) -> str:
#     """
#     Schedules a meeting.

#     Parameters:
#     - participants (str): List of attendees or team name.
#     - datetime (str): Meeting time.
#     - topic (str): Subject or agenda of the meeting.

#     Returns:
#     - str: Confirmation message.
#     """
#     return f"Meeting scheduled with {participants} on {datetime} about '{topic}'."

def schedule_meeting(participants: str, time: str, topic: str) -> str:
    """
    Schedules a meeting.

    Parameters:
    - participants (str): Attendees
    - time (str): Time of meeting
    - topic (str): Topic

    Returns:
    - str: Confirmation
    """
    return f"Meeting scheduled with {participants} on {time} about '{topic}'."
