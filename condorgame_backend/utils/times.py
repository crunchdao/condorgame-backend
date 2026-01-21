HOUR = 60 * 60
MINUTE = 60
DAY = 24 * HOUR


def format_seconds(seconds: int) -> str:
    """
    Format a given number of seconds into a human-readable format of days, hours, or minutes.
    
    Args:
        seconds (int): The number of seconds to format.

    Returns:
        str: The formatted string in days, hours, or minutes.
    """
    if seconds > DAY:
        return f"{seconds // DAY}d"
    elif seconds >= HOUR:
        return f"{seconds // HOUR}h"
    elif seconds >= MINUTE:
        return f"{seconds // MINUTE}m"
    else:
        return f"{seconds // MINUTE}s"
