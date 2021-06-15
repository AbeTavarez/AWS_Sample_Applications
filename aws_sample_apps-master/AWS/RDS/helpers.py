import datetime as dt


def date_time_converter(o):
    if isinstance(o, dt.datetime):
        return o.__str__()

