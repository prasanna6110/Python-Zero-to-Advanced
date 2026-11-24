# Day 101 · Sending Emails with smtplib and the email Package — Building a plain text and HTML email
# Run: python example_1.py

from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Your Python course progress"
msg["From"] = "course@example.com"
msg["To"] = "student@example.com"
msg.set_content("Hi! You completed 50 days. Keep going!")
msg.add_alternative("<h2>Hi!</h2><p>You completed <b>50 days</b>. Keep going! 🚀</p>", subtype="html")
print(msg.as_string()[:600])
