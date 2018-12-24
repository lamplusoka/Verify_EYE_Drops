#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

from_address = 'enter_from_gmailAdress'


def send_mail_to(pass_from_URL, to_address, message):
    password      = str(pass_from_URL)
    msg = MIMEText(message)
    msg['subject'] = 'Eye Drops Report'
    #smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpobj.ehlo()
    smtpobj.starttls
    smtpobj.ehlo
    smtpobj.login(from_address, password)
    smtpobj.sendmail(from_address, to_address, msg.as_string())
    smtpobj.quit()