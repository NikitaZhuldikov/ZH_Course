from utils.func import loading_file
import os
from utils.config import ROOT_DIR

def test_loading_file():
    test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    assert loading_file(test_path) == []
