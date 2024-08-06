from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.mailtrap.io',
    MAIL_PORT=2525,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.getenv('api'),
    MAIL_PASSWORD=os.getenv('3a54a1ecd19486e99614e5a57cf97b39')
)

mail = Mail(app)

@app.route('/send_test_email')
def send_test_email():
    try:
        msg = Message('Test Email', sender='dummy@example.com', recipients=['pooja.prp99@gmail.com'])
        msg.body = 'This is a test email sent from Flask.'
        mail.send(msg)
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
