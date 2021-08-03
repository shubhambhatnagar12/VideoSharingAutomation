import mysql.connector
from mysql.connector import Error
import os

def startDBconnection():
    try:
        connection = mysql.connector.connect(host='database-1.c0xxycpnulf5.us-east-1.rds.amazonaws.com',
                                         database='awsProject',
                                         user='admin',
                                         password=os.getenv('password'))
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            # cursor = connection.cursor()
            # cursor.execute("select database();")
            # record = cursor.fetchone()
         
            #print("You're connected to database: ", record)

        return connection

    except Error as e:
        print("Error while connecting to MySQL", e)
    # finally:
    #     if connection.is_connected():
    #         # cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")