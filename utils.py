from datetime import datetime

def get_day() -> int:
    """
    
    Get the current day as a int number
    
    """
    now = datetime.now()
    day = now.strftime("%d")
    return int(day)

def set_title() -> str:
    """
    
    Set the title in format current-day/count-of-days-of-year

    If the current is the first of year
    >>> set_title()
    01/365

    Returns:
        title: title of habits checks
    """
    day = get_day()
    return str(day) + "/365"


# assert set_title() == "9/365"