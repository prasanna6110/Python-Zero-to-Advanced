# Day 101 · Sending Emails with smtplib and the email Package — Sending through SMTP (with a fake server for testing)
# Run: python example_3.py

import smtplib, os
from email.message import EmailMessage
from unittest.mock import patch

def send_report(to, body):
    msg = EmailMessage()
    msg["Subject"], msg["From"], msg["To"] = "Daily report", "bot@example.com", to
    msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(os.environ.get("EMAIL_USER", "user"), os.environ.get("EMAIL_APP_PASSWORD", "app-pass"))
        s.send_message(msg)
    return msg

sent = []
with patch("smtplib.SMTP_SSL") as fake_smtp:          # no real email is sent
    fake_smtp.return_value.__enter__.return_value.send_message.side_effect = sent.append
    send_report("friend@example.com", "All systems normal ✅")
print("emails sent:", len(sent), "| to:", sent[0]["To"], "| body:", sent[0].get_content().strip())
print("For real sending: set EMAIL_USER and EMAIL_APP_PASSWORD and remove the patch.")
