import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'csar.bello25@gmail.com '
receiver_email = '491810476@gmail.com'
subject = 'Prueba'
body = 'Este correo fue mandado con Python'

# Set up the MIMEText and MIMEMultipart objects
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Establish a connection to the SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    # Start TLS (Transport Layer Security) for secure connection
    server.starttls()

    # Login to the email account
    server.login(sender_email, 'aarq dtnf xeoc xwns')

    # Send the email
    server.send_message(message)

print('Email sent successfully!')
