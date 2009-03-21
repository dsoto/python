#!/usr/bin/env python
'''
example of sending email using smtplib and email
'''

# configure email
fromAddress = 'a@gmail.com'
toAddress   = 'b@gmail.edu'
subject     = 'subject'
password    = 'password'
body        = 'python test mail'

# assemble MIME 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
msg = MIMEMultipart()
msg['From'] = fromAddress
msg['To'] = toAddress
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

# send over server
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromAddress, password)
server.sendmail(fromAddress, toAddress, text)
