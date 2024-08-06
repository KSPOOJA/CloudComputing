from flask_mail import Message
from extensions import mail

def send_email(subject, recipients, body):
  try:
    msg = Message(subject, sender='no-reply@example.com', recipients=recipients)
    msg.body = body
    mail.send(msg)
    return {"status_code": 200}
  except Exception as e:
    print(f"Failed to send email: {e}")
    return None
