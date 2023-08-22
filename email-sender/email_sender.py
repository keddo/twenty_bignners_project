# Go over to your email and setup 2 factor authentication
# Generate app password
# Create a function to send the mail

from email.message import EmailMessage
from password import password
import ssl
import smtplib

# Set the of the email and it's password
sender = "adu.kedir.abdurahman@gmail.com"
email_password = password

# Set the email receiver
receiver = "example@gmail.com"

# Main subject of the email
subject = "Please follow me on github/linkedin/twitter"

# Body of the email
body = """
    Let's connect each other to create influence and level up.
"""

# Create an instance of email message object
em = EmailMessage()
em['from'] = sender
em['to'] = receiver
em['subject'] = subject
em.set_content(body)