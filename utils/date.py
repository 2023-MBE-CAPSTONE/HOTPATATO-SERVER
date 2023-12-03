
from datetime import datetime


def get_today_date():
    today = datetime.now()
    today_date = today.strftime('%Y%m%d')
    return today_date