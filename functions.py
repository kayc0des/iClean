#function declaration module
import re
from email.message import EmailMessage
import ssl
import smtplib
import random
import schedule
import time

def user_info():
    global username, user_email, user_password
    username = input("Enter your username: ")
    user_email = input("Enter email: ")
    user_password = input("Enter password: ")
    check(user_email)

def check(email):

    regex =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if (re.fullmatch(regex, email)):
        pass
    else :
        print("Invalid email address")
        print("Enter an email of the form johndoe@gmail.com")
        user_info()


def email_verification(username, user_email, avcode):

    #global avcode
    #avcode = random.randrange(4010, 8010)

    email_sender = 'icleanapp.py@gmail.com'
    email_password = 'oovufvagresdoobg'
    email_receiver = user_email

    #define subject and body of the email
    subject = 'Verification Code'
    body = f"Hi {username}, Your verification code is {avcode}"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def reg_success(user_email, username):

    email_sender = 'icleanapp.py@gmail.com'
    email_password = 'oovufvagresdoobg'
    email_receiver = user_email

    subject = 'Hurray! Account Created'
    body = f"""Hi {username}, 
    You succesfully signed up to iClean App and your credentials have been added to the iclean database. Get Ready to receive daily emails from us on the need to keep your environment clean, tips on self and environmental hygiene.
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def daily_message(email):
    
    email_sender = 'icleanapp.py@gmail.com'
    email_password = 'oovufvagresdoobg'
    email_receiver = email

    subject = 'iClean: Reminder Demo'
    body = f"""Sample Email sent to all users"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


#automate message
def text_schedule():
    #job = schedule.every()day.at("10:00").do()

    while True:
        schedule.run_pending()
        time.sleep(1)