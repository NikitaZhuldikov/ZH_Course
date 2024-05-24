from utils import loading_file
import os
from config import ROOT_DIR

def test_loading_file():
    test_path = os.path.json(ROOT_DIR, 'tests', 'test_operations.json')
    assert loading_file(test_path) == []
