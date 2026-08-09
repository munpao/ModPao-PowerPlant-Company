#!/usr/bin/env python3
"""
contact_form.py - handles the "Contact us" form on the corporate site.
Emails the submission to our technical contact. Simple CGI-style script,
deployed alongside the static pages.

Credentials now come from the environment - see the MAILER_* vars below.
"""
import cgi, os, smtplib
from email.mime.text import MIMEText

SMTP_HOST = os.environ["MAILER_SMTP_HOST"]
SMTP_PORT = int(os.environ.get("MAILER_SMTP_PORT", "587"))
SMTP_USER = os.environ["MAILER_SMTP_USER"]
SMTP_PASS = os.environ["MAILER_SMTP_PASS"]
TO_ADDR   = os.environ["MAILER_TO_ADDR"]


def send(name, email, message):
    body = f"From: {name} <{email}>

{message}"
    msg = MIMEText(body)
    msg["Subject"] = "Website contact form submission"
    msg["From"] = SMTP_USER
    msg["To"] = TO_ADDR
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)


def main():
    form = cgi.FieldStorage()
    send(form.getvalue("name", ""), form.getvalue("email", ""), form.getvalue("message", ""))
    print("Content-Type: text/html
")
    print("<p>Thanks — we'll be in touch.</p>")


if __name__ == "__main__":
    main()
