from utils.func import loading_file
import os
from utils.config import TEST_PATH

def test_loading_file():
    file = os.path.join(TEST_PATH, 'test_operations.json')
    assert loading_file(file) == []
