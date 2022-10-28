
import requests 

def get_data_from_ona():
    url = input('Enter the url:')
    auth = (str(input('Enter you username:')), str(input('Enter your password:')))
    response =requests.get(url=url,auth=auth)
    
    if response.status_code==200:
        ona_data= response.json()
        return ona_data

    else:
        print(response.status_code)
        print(response.text)

p = get_data_from_ona()
print(p)
