import mysql.connector
from dotenv import dotenv_values
import os
import json
import requests
import base64


energetica_db_config_b64 = os.getenv("ENERGETICA_DB_CONFIG")
cels_db_config_b64 = os.getenv("CELS_DB_CONFIG")
if not energetica_db_config_str or not cels_db_config_str:
    raise ValueError("Database configuration secrets are missing.")
energetica_db_config = json.loads(base64.b64decode(energetica_db_config_b64).decode("utf-8"))
cels_db_config = json.loads(base64.b64decode(cels_db_config_b64).decode("utf-8"))

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")



def get_db_connection(database):
    db_config = cels_db_config if database == "cels" else energetica_db_config
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as e:
        print("Error:", e)
        return None


def get_db_query_result(sql_query, database="energetica"):
    connection = get_db_connection(database)
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchone(
        )[0] if database == "energetica" else dict(zip([column[0] for column in cursor.description], cursor.fetchone()))
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
