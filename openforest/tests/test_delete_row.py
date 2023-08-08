"""
pytest --dataset_name='PULL_REQUEST_TEMPLATE.yml' test_add_row.py
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

def test_delete_row(new_dataset):
    # Hypothesis: add_row works
    new_dataset_name = new_dataset['dataset_name']
    openforest = OpenForestDatabase()
    init_len_openforest = len(openforest)
    openforest.add_row(new_dataset)
    assert len(openforest) == init_len_openforest+1
    assert new_dataset_name in list(openforest.get.index)
    openforest.delete_row(new_dataset_name)
    assert len(openforest) == init_len_openforest
    assert new_dataset_name not in list(openforest.get.index)

