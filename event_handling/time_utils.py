import time
import datetime

def parse_date(date):
    return int(time.mktime(time.strptime(date, "%m/%d/%Y %H:%M"))*1000)

def get_current_utc_time():
    now = datetime.datetime.utcnow()
    return int((now - datetime.datetime(1970, 1, 1)).total_seconds())