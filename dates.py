from datetime import datetime

def string_to_date(string):
    date_format = '%Y-%m-%d'
    datetime_obj = datetime.strptime(string, date_format)
    return datetime_obj.date()