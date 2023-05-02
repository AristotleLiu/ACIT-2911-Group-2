from datetime import datetime

date_format = '%Y-%m-%d'

def string_to_date(string):
    datetime_obj = datetime.strptime(string, date_format)
    return datetime_obj.date()