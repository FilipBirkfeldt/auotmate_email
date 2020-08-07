# script for sending emails

import email
import smtplib 
import ssl

from datetime import date, datetime

import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if (date.today().weekday() == 0) or (date.today().weekday() == 4): 
    port = 465  # For SSL
    password = input("Type your password and press enter: ")
    #password = 'password'
    sender_email = '@gmail.com'
    rec_email = ''

    # Files to send 
    pdf1 = ''
    pdf2 = ''
    files = [pdf1, pdf2]

    # MAIL-CONTENT
    subject = ""
    body = '''
            '''

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = rec_email
    message["Subject"] = subject
    # message["Bcc"] = rec_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    for filename in files:
        f = filename
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        message.attach(part)

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, text)

else: 
    print('not sending out mails today')
    


