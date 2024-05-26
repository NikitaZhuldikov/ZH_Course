import pytest
from utils.func import loading_file, filter_list, sorts_date, get_date, hidden_number
import os
from utils.config import TEST_PATH

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 4, "state": "EXECUTED", "date": "2018-04-01T00:00:00.000001"}
]
@pytest.fixture
def operations_fixture():
    return operations

file = os.path.join(TEST_PATH, 'test_operations.json')

def test_loading_file():
    assert loading_file(file) == []

def test_filter_list(operations_fixture):
    assert len(filter_list(operations_fixture)) == 3

def test_sorts_date(operations_fixture):
    assert [i["id"] for i in sorts_date(operations_fixture)] == [4, 3, 2, 1]

def test_get_date():
    assert get_date("2018-01-01T00:00:00.000000") == "01.01.2018"

def test_hidden_number():
    assert hidden_number("Visa Classic 7756673469642839") == "Visa Classic 7756 67** **** 2839"
    assert hidden_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert hidden_number("Счет 75106830613657916952") == "Счет **6952"