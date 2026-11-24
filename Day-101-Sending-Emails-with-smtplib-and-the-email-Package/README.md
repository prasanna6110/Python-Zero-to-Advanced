# Day 101 · Sending Emails with smtplib and the email Package

_Advanced_

## Building an email
```python
from email.message import EmailMessage
msg = EmailMessage()
msg["Subject"] = "Hello"
msg["From"] = "me@gmail.com"
msg["To"] = "you@gmail.com"
msg.set_content("Plain text body")
msg.add_alternative("<h1>HTML body</h1>", subtype="html")
msg.add_attachment(data, maintype="application", subtype="pdf", filename="report.pdf")
```
## Sending it
```python
import smtplib, ssl, os
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as s:
    s.login(os.environ["EMAIL_USER"], os.environ["EMAIL_APP_PASSWORD"])
    s.send_message(msg)
```
- For Gmail, enable 2-step verification and create an **App Password**. Never use your real password in code.
- Keep your credentials in **environment variables**.
- You can test locally with a fake server: `python -m aiosmtpd -n -l localhost:1025` (needs `pip install aiosmtpd`).

> The examples build real emails and "send" them to an in-memory list, so no credentials are needed.

## Examples

### Example 1: Building a plain text and HTML email  ([`example_1.py`](example_1.py))

```python
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Your Python course progress"
msg["From"] = "course@example.com"
msg["To"] = "student@example.com"
msg.set_content("Hi! You completed 50 days. Keep going!")
msg.add_alternative("<h2>Hi!</h2><p>You completed <b>50 days</b>. Keep going! 🚀</p>", subtype="html")
print(msg.as_string()[:600])
```

### Example 2: Attachments and parsing an email back  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Sending through SMTP (with a fake server for testing)  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Send yourself a daily quote email (use a Gmail App Password).
2. Email a CSV report generated from a SQLite database.
3. Send personalised emails to a list of contacts read from a CSV (a mail merge).

---

[⬅ Day 100](../Day-100-Web-Scraping-and-HTML-Parsing/README.md) · [🏠 Home](../README.md) · [Day 102 ➡](../Day-102-Working-with-Excel-PDF-and-Images-Popular-Libraries/README.md)
