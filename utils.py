from datetime import datetime

def get_date():
    now = datetime.now()
    return now

def get_day(date) -> int:
    """
    
    Get the current day as a int number
    
    """
    day = date.strftime("%j")
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
    day = get_day(get_date())
    return str(day) + "/366"

