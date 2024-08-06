import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:CloudComputing2024@mydatabase.cvca4k4ky46o.us-east-1.rds.amazonaws.com/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # MAIL_USERNAME = os.environ.get('p08228412@gmail.com')
    # MAIL_PASSWORD = os.environ.get('K923@xtz')
    BCRYPT_LOG_ROUNDS = 12
    # MAILGUN_DOMAIN = 'mail.faizan.me'
    # MAILGUN_SECRET = '080ceaeac64781fe612547c579f684aa-a26b1841-f0355abf'
    # MAILGUN_ENDPOINT ='api.mailgun.net'
    #STRIPE_SECRET_KEY = 'sk_test_51PkZBlLDL5c2IwMGBTkGHgafWWkUaCllyyoQBIkmaY3fPYbwy07Q23SSHFyoX5lXIXKNpIJbYQs5dqKlbyjkAqFs00sFaKj9ZH'
    # PAYPAL_CLIENT_ID = os.environ.get('AXURJtLil9b5BuDZ47xdEY8yC4YajOfga6y-UhsdrDQWejzAJp2uMtYCTzq47bJpJibJXyBKekxs_Pfv')
    # PAYPAL_CLIENT_SECRET = os.environ.get('EAelqwGufFWrjZCtKcv8gTUrB-pEo98Bz49IjszNBSbkFO5qubXo-0qn58vn0D9krX6Qxk6gpeJzjtEJ')
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '47a9c9d4058dff'
    MAIL_PASSWORD = 'f2d3fa99cc42a3'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
