from dbconn import add_message

print("iClean Admin")

admin_email = input("Enter admin Email: ")
admin_password = input("Enter admin password: ")

email = 'icleanapp.py@gmail.com'
password = 'icleanAPP'

if admin_email == email and admin_password == password:
    pass
else:
    print("Invalide Credentials")
    quit()

adminName = input("Enter admin Name: ")
message = input("Enter submission message: ")
msg_dic = {'adminName': adminName, 'message': message}
add_message(msg_dic['message'], msg_dic['adminName'])
