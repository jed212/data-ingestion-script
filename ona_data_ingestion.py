import os
import requests
import csv

from dotenv import load_dotenv

load_dotenv(dotenv_path=f"compose1.env")

URL = os.getenv("URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def get_data_from_ona():
    response=requests.get(url=URL,auth=(USERNAME, PASSWORD))
    
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


