from functions import check
from functions import email_verification
from functions import reg_success
import functions
import random
from dbconn import registerUser
from dbconn import checkUser
import maskpass
from dbconn import existingUser
from dbconn import email_records
from dbconn import fetch_message
from functions import daily_message
import schedule
import time

print("iClean App")

def start():
    global sign_log
    sign_log = input("Do you have an account? Yes/No ")

start()

if sign_log == 'NO' or sign_log == 'no' or sign_log == 'No':
    global name
    name = input("Enter name: ")
    print(f"""Hello, {name} Welcome to iClean App. iClean app is an app developed by OurName 
    that sends daily emails to users on the need to keep their environment clean.""")

    resp = input("Do you wish to continue?: Yes?No ")

    if resp == 'Yes' or resp == 'yes' or resp == 'ye' or resp == 'y':
        print("Great! Lets get you started!")
    else :
        print("Sad to see you leave")
        quit()

    def user_info():
        global username, user_email, user_password
        username = input("Enter your username: ")
        user_email = input("Enter email: ")
        user_password = maskpass.askpass(prompt="Enter password:", mask="*")
        check(user_email)
        user_details = {'user_email': user_email, 'user_password': user_password}
        existingUser(user_details['user_email'])


    #collect user info, verify and insert into database
    user_info()
    user_details = {'name': name, 'username': username, 'user_email': user_email, 'user_password': user_password}
    avcode = random.randrange(4010, 8010)
    email_verification(user_details['username'], user_details['user_email'], avcode)
    verification_code = int(input("Enter the verification code sent to you: "))
    if avcode == verification_code:
        registerUser(name, user_details['username'], user_details['user_email'], user_details['user_password'])
        reg_success(user_details['user_email'], user_details['username'])
    else:
        print("Invalid Verification Code")
        quit()
else:
    print("Please log in")
    user_email = input("Enter email: ")
    user_password = maskpass.askpass(prompt="Enter password:", mask="*")

    user_details = {'user_email': user_email, 'userpassword': user_password}

    #check if entry is present in database
    checkUser(user_details['user_email'], user_details['userpassword'])

#Fetch emails and messages and save them as objects
email_rec = email_records()
print(email_rec)
message_rec = fetch_message()
print(message_rec)

daily_message(email_rec)

#automate message to be sent at 10AM everyday
def text_schedule():
    #job = schedule.every()day.at(10:00).do()

    while True:
        schedule.run_pending()
        time.sleep(1)