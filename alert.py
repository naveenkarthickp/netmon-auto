import yagmail

def send_email_alert(to, subject, body):
    yag = yagmail.SMTP('your_gmail@gmail.com', 'your_app_password')
    yag.send(to=to, subject=subject, contents=body)
