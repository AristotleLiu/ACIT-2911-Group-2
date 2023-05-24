from datetime import datetime


def string_to_date(string):
    """
    Convert a string in the format 'YYYY-MM-DD' to a date object.

    Args:
        string (str): A string representing a date in the format 'YYYY-MM-DD'.

    Returns:
        datetime.date or None: A date object if the string is in the correct format,
        None if the string is empty or None.
    """
    date_format = "%Y-%m-%d"
    if string:
        datetime_obj = datetime.strptime(string, date_format)
        return datetime_obj.date()
    else:
        return None
