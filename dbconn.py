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


def checkUser(useremail, userpassword):
    try:
        conn = mysql.connector.connect(host='localhost', database='icleandb', user='root', password='kayc0des')
        print("Hi")

    except Error as e:
        print("Sorry", e)
    finally:
        if conn.is_connected():
            conn.close()
