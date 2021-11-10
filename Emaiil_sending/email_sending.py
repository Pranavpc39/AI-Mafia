import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():

    senders_email = "pc239chougule@gmail.com"
    password = getpass.getpass()
    print(password)
    subject = 'This email sending by Python'
    msg = '''

        This is the mail that i am sending to my another the email account by using python. Hope it will succeed.

        Thank You,
                    Pranav Chougule
    '''
    # server initialization
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senders_email, password)

    # drafting the message

    msg = MIMEText(msg)
    msg['From'] = senders_email
    msg['Subject'] = subject
    msg['To'] = 'pc39chougule@gmail.com'
    recipeints = 'pc39chougule@gmail.com'

    server.sendmail(senders_email, recipeints, msg.as_string())


send_email()
