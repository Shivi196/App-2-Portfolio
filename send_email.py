import smtplib,ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    sender_email = "sharmabruno310@gmail.com"
    sender_password = os.getenv("PASSWORD")
    user_email = "sharmabruno310@gmail.com"

#     message = '''\
# Subject : Test Email
# In the context of secure communication, an SSL Context is a collection of settings and configurations that define the parameters for establishing a secure connection using SSL/TLS protocols.
# '''
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, user_email, message)





