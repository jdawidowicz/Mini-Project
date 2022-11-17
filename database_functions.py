import pymysql
import os
from dotenv import load_dotenv


def connect():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")


    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    return connection

def disconnect(cursor,connection):
    cursor.close()
    connection.close()