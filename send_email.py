#!/usr/bin/env python
"""created on 2021-01-21"""

import argparse
import json
import os
import pathlib
import ssl
import random

from collections import defaultdict

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from markdown import Markdown
from smtplib import SMTP


def main():
    password = os.getenv('SMTP_PASS')
    host = os.getenv('SMTP_HOST')
    from_email = os.getenv('EMAIL_FROM')
    to_email = os.getenv('EMAIL_TO')
    error_msg = 'Please add SMTP_PASS, SMTP_HOST, EMAIL_FROM, and EMAIL_TO as env vars'
    text = os.getenv('THREE_YEAR_PAINTED_PICTURE')
    assert all([text, password, host, from_email, to_email]), error_msg

    message = MIMEMultipart("alternative")
    message["Subject"] = f"{datetime.now().strftime('%Y-%m-%d')} Daily Painted-Picture-Vision Reminder"
    message["From"] = from_email
    message["To"] = to_email

    # Create the plain-text and HTML version of the email
    text = text.replace('\\n', '\n')
    markdowner = Markdown()
    html = markdowner.convert(text)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with SMTP(host=host, port=587) as server:
        server.starttls(context=context)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())
        print(f'sent email at {datetime.now()}')


if __name__ == "__main__":
    main()

