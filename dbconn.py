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

def add_message(message):
    try:
        conn = mysql.connector.connect(host='localhost', database='icleandb', user='root', password='kayc0des')
        admin_insert_query = """INSERT INTO MessageTable (Message) VALUES (%s) """
        record = (message)
        cursor = conn.cursor()
        cursor.execute(admin_insert_query, record)
        conn.commit() 
        print("Succesful Registration")
        cursor.close
    except Error as e:
        print("Sorry, we encountered an error", e)
    finally:
        if conn.is_connected():
            conn.close()


def checkUser(useremail):
    try:
        conn = mysql.connector.connect(host='localhost', database='icleandb', user='root', password='kayc0des')
        search_query = """SELECT * FROM UserTable WHERE Useremail=%s"""
        record = useremail
        cursor = conn.cursor()
        my_cursor = cursor.execute(search_query, record)
        my_row = cursor.fetchall()
        print(my_row[1])

    except Error as e:
        print("Sorry", e)
    finally:
        if conn.is_connected():
            conn.close()
