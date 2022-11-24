import mysql.connector 
from mysql.connector import Error

def registerUser(name, username, useremail, userpassword):
    try:
        conn = mysql.connector.connect(host='localhost', database='icleandb', user='root', password='kayc0des')
        user_insert_query = """INSERT INTO UserTable (Name, Username, UserEmail, UserPassword)
                            VALUES
                            (%s, %s, %s, %s) """
        record = (name, username, useremail, userpassword)
        cursor = conn.cursor()
        cursor.execute(user_insert_query, record)
        conn.commit() 
        print("Succesful Registration")
        cursor.close

    except Error as e:
        print("Sorry, we encountered an error", e)
    finally:
        if conn.is_connected():
            conn.close()

def add_message(message, admin_name):
    try:
        conn = mysql.connector.connect(host='localhost', database='icleandb', user='root', password='kayc0des')
        admin_insert_query = """INSERT INTO MessageTable (Message, adminName) VALUES (%s, %s) """
        record = (message, admin_name)
        cursor = conn.cursor()
        cursor.execute(admin_insert_query, record)
        conn.commit() 
        print("Succesful Submission")
        cursor.close
    except Error as e:
        print("Sorry, we encountered an error", e)
    finally:
        if conn.is_connected():
            conn.close()


def checkUser(useremail, userpassword):
    try:
        conn = mysql.connector.connect(host='localhost', database='icleandb', user='root', password='kayc0des')
        search_query = """SELECT * FROM UserTable WHERE UserEmail=%s AND UserPassword=%s"""
        record = (useremail, userpassword)
        cursor = conn.cursor()
        cursor.execute(search_query, record)
        result = cursor.fetchall()
        if result == []:
            print("Error: Credentials Not Found!")
        else:
            pass

    except Error as e:
        print("Sorry", e)
    finally:
        if conn.is_connected():
            conn.close()


def existingUser(useremail, userpassword):
    try:
        conn = mysql.connector.connect(host='localhost', database='icleandb', user='root', password='kayc0des')
        search_query = """SELECT * FROM UserTable WHERE UserEmail=%s AND UserPassword=%s"""
        record = (useremail, userpassword)
        cursor = conn.cursor()
        cursor.execute(search_query, record)
        result = cursor.fetchall()
        if result == []:
            pass
        else:
            print("You already have an account!")
            print("Please Log in")

    except Error as e:
        print("Sorry", e)
    finally:
        if conn.is_connected():
            conn.close()
