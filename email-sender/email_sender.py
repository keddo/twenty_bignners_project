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
