# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))
DATA_DIR = os.path.join(TEST_PATH, "data")

from pydaily.filesystem import batch_rename_files

def test_batch_rename_files():
    input_dir = os.path.join(DATA_DIR, 'input')
    save_dir = os.path.join(DATA_DIR, 'output')
    batch_rename_files(input_dir, save_dir, start_num=5)
