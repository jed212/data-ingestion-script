'''import modules'''
from script_to_db import evaluate_json_values, fetch_data


def test_evaluate_json_values():
    '''Testing evaluate_json_values()'''
    data_to_use = [
        {
            "_id": 2334,
            "_submitted_by": "Tom",
            "specific_time": "23:30:00.000+03:00"
        },
        {
            "_id": 1113,
            "_submitted_by": "Tom",
            "specific_time": None
        },
        {
            "_id": 2379,
            "_submitted_by": "Tom",
            "specific_time": "07:00:00.000+03:00"
         }
        ]
    my_list = evaluate_json_values(data_to_use)
    assert len(my_list) == 3
    assert list(zip(*my_list))[0] == (2334, 1113, 2379)

    
def test_fetch_data():
    '''testing data fetched'''
    url = "my_url"
    ona_auth = ("username", "password")
    dict_list = fetch_data(url, ona_auth)
    assert isinstance(dict_list, list)
