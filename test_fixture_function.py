import pytest
import json
import logging
from json import JSONDecodeError

@pytest.fixture()

def read_config():
    
    global config
    
    try:
     with open("app.json") as f:
        #app.json is a empty JSON file
        config = json.load(f)
    except json.decoder.JSONDecodeError:
        print("Error in file/json")

        logging.info("Read config")
        return config

def test1(read_config):
    logging.info("Test function 1")
    assert read_config == {}

def test2(read_config):
    logging.info("Test function 2")
    assert read_config == {}

