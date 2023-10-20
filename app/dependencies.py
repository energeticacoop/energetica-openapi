import mysql.connector
from dotenv import dotenv_values
import os
import requests

script_dir = os.path.dirname(__file__)
db_config = dotenv_values(os.path.join(script_dir, ".env.db"))
google_api_key = dotenv_values(os.path.join(script_dir, ".env.googleapikey"))[
    "GOOGLE_API_KEY"]


def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as e:
        print("Error:", e)
        return None


def get_db_query_result(sql_query):
    connection = get_db_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchone()[0]
    except mysql.connector.Error as e:
        print("Error:", e)
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return result


def get_json_from_google_spreadsheet_api(spreadsheet_id, named_range):
    api_url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{named_range}?key={google_api_key}'
    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # This will raise an exception for non-200 status codes

        # Parse the JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        # Handle general request exceptions
        raise e
