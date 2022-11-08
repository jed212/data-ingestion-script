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
    ona_database_file=response.json()
    return ona_database_file
 

def create_table():
    commands=('CREATE TABLE IF NOT EXISTS test_2(_id int primary key NOT NULL,_submitted_by varchar NOT NULL,specific_time time);')
    conn=None
    try:
        connection=psycopg2.connect(user=USER,password=PASSWORD,host=HOST,port=PORT,database=DATABASE)
        conn=connection.cursor()
        
        if connection:
            print('success')
        conn.execute(commands)
        connection.commit()
        connection.close()
    except Exception as error:
        print(error)
  

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


def insert_statement(table_values):
    tupl_lst= [tuple (x) for x in table_values]
    conn=None
    try:
        connection=psycopg2.connect(user=USER,password=PASSWORD,host=HOST,port=PORT,database=DATABASE)
        conn=connection.cursor()
        if connection:
            print('success')
        for x in tupl_lst:
           insert_command=f'insert into test_2(_id,_submitted_by,specific_time) values(%s,%s,%s)'
           conn.execute(insert_command,x)
        connection.commit()
        connection.close()
    except Exception as error:
        print(error)
    print(insert_command)
    

if __name__ == '__main__':
    create_table()
    table_values=evaluate_json_values()
    insert_statement(table_values)