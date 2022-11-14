'''import modules'''
import psycopg2
from script_to_db import connection_to_db, evaluate_json_values
from script_to_db import fetch_data, USER, PASSWORD, HOST, PORT, DATABASE


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
    # assert my_list[0]


def test_connection_to_db():
    '''testing connection to the database'''
    connection = psycopg2.connect(
        user=USER, password=PASSWORD,
        host=HOST, port=PORT,
        database=DATABASE)
    connection_to_db()
    assert connection is not None


def test_fetch_data():
    '''testing data fetched'''
    url = "my_url"
    ona_auth = ("username", "password")
    dict_list = fetch_data(url, ona_auth)
    assert ("_id" in entry for entry in dict_list)
    assert ("_submitted_by" in entry for entry in dict_list)
    assert ("specific_time" in entry for entry in dict_list)
