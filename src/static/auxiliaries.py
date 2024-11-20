from datetime import datetime
from src.static.constants import DATE_FORMAT

def get_actual_date():
    return datetime.now().strftime(DATE_FORMAT)