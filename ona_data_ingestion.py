import os
import requests 
from dotenv import load_dotenv

load_dotenv(dotenv_path=f"compose1.env")

URL = os.getenv("URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
def get_data_from_ona():
    auth = (USERNAME, PASSWORD)
    response =requests.get(url=URL,auth=auth)
    
    if response.status_code==200:
        ona_data= response.json()
        return ona_data

    else:
        print(response.status_code)
        print(response.text)

p = get_data_from_ona()
print(p)
