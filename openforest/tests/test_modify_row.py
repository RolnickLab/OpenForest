"""
pytest --dataset_file='test_dataset_example.yml' test_modify_row.py
"""
import yaml
import pandas as pd
import pytest
from pytest import fixture

from openforest.utils import OPENFOREST_HOME
from openforest.scripts.openforest_database import OpenForestDatabase

@fixture
def new_dataset(dataset_file):
    path = OPENFOREST_HOME / dataset_file
    with open(path, 'r') as stream:
        try:
            dataset_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dataset_file

def test_modify_row(new_dataset):
    # Hypothesis: add_row and delete_row work
    modified_dataset_name = new_dataset['dataset_name']
    openforest = OpenForestDatabase()
    assert modified_dataset_name in list(openforest.get.index)
    openforest.modify_row(new_dataset)
    assert modified_dataset_name in list(openforest.get.index)
