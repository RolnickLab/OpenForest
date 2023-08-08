"""
pytest --dataset_name='PULL_REQUEST_TEMPLATE.yml' test_erase.py

Note that this test will not be run at each commit.
It's only to test the class method
"""
import yaml
import pandas as pd
import pytest
from pytest import fixture

from openforest.utils import OPENFOREST_HOME
from openforest.scripts.openforest_database import OpenForestDatabase

@fixture
def new_dataset(dataset_name):
    path = OPENFOREST_HOME / dataset_name
    with open(path, 'r') as stream:
        try:
            dataset_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dataset_file

def test_erase(new_dataset):
    new_dataset_name = new_dataset['dataset_name']
    openforest = OpenForestDatabase()
    openforest.add_row(new_dataset)
    openforest.erase
