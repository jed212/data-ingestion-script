'''import modules'''
from unittest.mock import patch
from script_to_db import evaluate_json_values


@patch('script_to_db.fetch_data')
def test_evaluate_json_values_from_fetch_data(mock_get):
    mock_get.return_value = [
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
    json_list = mock_get.return_value
    assert evaluate_json_values(json_list) == [
        [2334, "Tom", "23:30:00.000+03:00"],
        [1113, "Tom", None],
        [2379, "Tom", "07:00:00.000+03:00"]
        ]
