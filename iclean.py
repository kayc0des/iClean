from functions import check
from functions import email_verification
from functions import reg_success
import functions
import random
from dbconn import registerUser
from dbconn import checkUser

print("iClean App")

sign_log = input("Do you have an account? Yes/No ")
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
        user_password = input("Enter password: ")
        check(user_email)

    #collect user info, verify and insert into database
    user_info()
    user_details = {'name': name, 'username': username, 'user_email': user_email, 'user_password': user_password}
    avcode = random.randrange(4010, 8010)
    email_verification(user_details['username'], user_details['user_email'], avcode)
    verification_code = int(input("Enter the verification code sent to you: "))
    if avcode == verification_code:
        if registerUser(name, user_details['username'], user_details['user_email'], user_details['user_password']):
            reg_success(user_details['user_email'], user_details['username'])
    else:
        print("Invalid Verification Code")
        quit()
else:
    print("Please log in")
    user_email = input("Enter email: ")
    user_password = input("Enter password: ")

    user_details = {'user_email': user_email, 'userpassword': user_password}

    #check if entry is present in database
    checkUser(user_details['user_email'])

