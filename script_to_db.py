
import psycopg2
import os
import requests
from dotenv import load_dotenv


load_dotenv(dotenv_path=f"compose1.env")

USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
HOST=os.getenv("HOST")
PORT=os.getenv("PORT")
DATABASE=os.getenv("DATABASE")
URL = os.getenv("URL")
ONA_USERNAME = os.getenv("ONA_USERNAME")
ONA_PASSWORD = os.getenv("ONA_PASSWORD")
ona_auth=(ONA_USERNAME,ONA_PASSWORD)

def fetch_data():
    response=requests.get(url=URL,auth=ona_auth)
    return response.json()
  

def create_table():
    commands=('CREATE TABLE IF NOT EXISTS test_2(_id int primary key NOT NULL,_submitted_by varchar NOT NULL,specific_time time);')
    execute_statements(commands)
    return 


def insert_statements():
    table_values=evaluate_json_values()
    tupl_lst= [tuple (x) for x in table_values]
    for x in tupl_lst:
        insert_command=f'insert into test_2(_id,_submitted_by,specific_time) values(%s,%s,%s);'
        execute_statements(insert_command,*x)
    return 


def connection_to_db(): 
    try:
        connection=psycopg2.connect(user=USER,password=PASSWORD,host=HOST,port=PORT,database=DATABASE)
    except Exception as error:
        print(error)
    return connection


def execute_statements(sql_command,*placeholder_values):
    try:
        connection=connection_to_db()
        conn=connection.cursor()
        if placeholder_values is None:
            conn.execute(sql_command)
            connection.commit()
        if placeholder_values is not None:
            conn.execute(sql_command,placeholder_values)
            connection.commit()
        close_connection(connection)
    except Exception as error:
        print(error)
    return


def close_connection(connection):
    if connection is not None:
        connection.close()
        

def evaluate_json_values():
    a=fetch_data()
    var_list=[]
    for entry in a:
        first_value=entry["_id"]
        second_value=entry["_submitted_by"]
        third_value=entry.get("specific_time")
        
        values_to_insert=[(first_value),(second_value),(third_value)]
        
        var_list.append(values_to_insert)

    return var_list
    

if __name__ == '__main__':
    create_table()
    insert_statements()