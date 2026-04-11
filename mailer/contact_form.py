#!/usr/bin/env python3
"""
contact_form.py - handles the "Contact us" form on the corporate site.
Emails the submission to our technical contact. Simple CGI-style script,
deployed alongside the static pages.
"""
import cgi, smtplib
from email.mime.text import MIMEText

SMTP_HOST = "mail.modpao-powerplant.com"
SMTP_PORT = 587
# credential user:pass
SMTP_USER = "wichai.t@modpao-powerplant.com"
SMTP_PASS = "W1chai#OT2025"
TO_ADDR   = "wichai.t@modpao-powerplant.com"


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
    print("Content-Type: text/html\n")
    print("<p>Thanks — we'll be in touch.</p>")


if __name__ == "__main__":
    main()
