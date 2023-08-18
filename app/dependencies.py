import mysql.connector
from dotenv import dotenv_values
import os

script_dir = os.path.dirname(__file__)
dotenv_path = os.path.join(script_dir, ".env")
db_config = dotenv_values(dotenv_path)


def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as e:
        print("Error:", e)
        return None
