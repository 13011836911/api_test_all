"""
__time__:2021/2/20 15:58
__author__:songshijie
"""

import pytest
import os
import allure
from base.mysql_operate import db
from base.read_data import data
from base.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "json_config", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data

api_data = get_data("api_test_data.yml")