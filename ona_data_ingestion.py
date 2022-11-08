
import os
import psycopg2
import requests

from dotenv import load_dotenv

connection=psycopg2.connect(user="favour",password="jedidiahfavour",port="5432",database="new_db")
cursor=connection.cursor()

load_dotenv(dotenv_path=f"compose1.env")

URL = os.getenv("URL")
ONA_USERNAME = os.getenv("ONA_USERNAME")
PASSWORD = os.getenv("PASSWORD")

def get_data_from_ona():
    response=requests.get(url=URL,auth=(ONA_USERNAME, PASSWORD))
    
    if response.status_code==200:
        ona_data= response.json()
        

        with open("new_csv_file","w", encoding="utf-8") as f:
            writer= csv.writer(f)
            count=0
            for cnt in ona_data:
                
                if count== 0:
                    header =cnt.keys()
                    writer.writerow(header)
                    writer.writerow(cnt.values())

                    count=count+1

                    
                elif count>=1:
                    writer.writerow(cnt.values())
            return 
    else:
        print(response.status_code)
        print(response.text)
get_data_from_ona()
print("Success")


