'''Imported modules'''
import os
import psycopg2
import requests
from dotenv import load_dotenv


load_dotenv(dotenv_path=f'{"compose1.env"}')

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")
url = os.getenv("URL")
ONA_USERNAME = os.getenv("ONA_USERNAME")
ONA_PASSWORD = os.getenv("ONA_PASSWORD")
ona_auth = (ONA_USERNAME, ONA_PASSWORD)


def fetch_data(page_url, page_auth):
    '''Function to get response from ona api in json format'''
    response = requests.get(url=page_url, auth=page_auth, timeout=10)
    return response.json()


def create_table():
    '''Command to create a table in the postgres database'''
    commands = '''CREATE TABLE IF NOT EXISTS test_2(
        _id int primary key NOT NULL,
        _submitted_by varchar NOT NULL,
        specific_time time);'''
    execute_statements(commands)


def insert_statements():
    '''Generating insert statement to populate table in postgres'''
    tupl_lst = [tuple(x) for x in table_values]
    for lst in tupl_lst:
        insert_command = f'{"insert into test_2(_id,_submitted_by,specific_time)values(%s,%s,%s);"}'
        execute_statements(insert_command, *lst)


def connection_to_db():
    '''Function to connect to the postgres database'''
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            database=DATABASE
            )
    except ValueError as error:
        print(error)
    return connection


def execute_statements(sql_command, *placeholder_values):
    '''Function to execute commands'''
    try:
        connection = connection_to_db()
        conn = connection.cursor()
        if placeholder_values is None:
            conn.execute(sql_command)
            connection.commit()
        if placeholder_values is not None:
            conn.execute(sql_command, placeholder_values)
            connection.commit()
        close_connection(connection)
    except ValueError as error:
        print(error)


def close_connection(connection):
    '''Function to close the connection to postgres'''
    if connection is not None:
        connection.close()


def evaluate_json_values(jsn_list):
    '''Function to generate value list'''
    var_list = []
    for entry in jsn_list:
        first_value = entry["_id"]
        second_value = entry["_submitted_by"]
        third_value = entry.get("specific_time")

        values_to_insert = [(first_value), (second_value), (third_value)]
        var_list.append(values_to_insert)
    return var_list


if __name__ == '__main__':
    connection_to_db()
    create_table()
    fetched_data = fetch_data(url, ona_auth)
    table_values = evaluate_json_values(fetched_data)
    insert_statements()
