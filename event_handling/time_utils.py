import time
import datetime

def parse_date(date, from_gui=False):
    format_string = "%Y-%m-%d %H:%M" if from_gui else "%m/%d/%Y %H:%M"
    return int(time.mktime(time.strptime(date, format_string))*1000)

def get_current_utc_time():
    now = datetime.datetime.utcnow()
    return int((now - datetime.datetime(1970, 1, 1)).total_seconds())