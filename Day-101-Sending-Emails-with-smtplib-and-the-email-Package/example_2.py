# Day 101 · Sending Emails with smtplib and the email Package — Attachments and parsing an email back
# Run: python example_2.py

from email.message import EmailMessage
from email import message_from_bytes, policy
import csv, io

buf = io.StringIO()
csv.writer(buf).writerows([["name", "marks"], ["Asha", 91], ["Ravi", 78]])
msg = EmailMessage()
msg["Subject"] = "Marks report"
msg["From"], msg["To"] = "teacher@example.com", "hod@example.com"
msg.set_content("Please find the report attached.")
msg.add_attachment(buf.getvalue().encode(), maintype="text", subtype="csv", filename="marks.csv")

raw = msg.as_bytes()
parsed = message_from_bytes(raw, policy=policy.default)
print("Subject:", parsed["Subject"])
for part in parsed.iter_attachments():
    print("Attachment:", part.get_filename(), "->", part.get_content().splitlines())
