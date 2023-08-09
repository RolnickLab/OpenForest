"""
pytest --dataset_name='Cactus Aerial Photos' test_delete_row.py
"""
import yaml
import pandas as pd
import pytest
from pytest import fixture

from openforest.utils import OPENFOREST_HOME
from openforest.scripts.openforest_database import OpenForestDatabase

@fixture
def get_dataset_name(dataset_name):
    print(dataset_name)
    return dataset_name

def test_delete_row(get_dataset_name):
    dataset_name_to_remove = get_dataset_name
    openforest = OpenForestDatabase()
    init_len_openforest = len(openforest)
    openforest.delete_row(dataset_name_to_remove)
    assert len(openforest) == init_len_openforest-1
    assert dataset_name_to_remove not in list(openforest.get.index)

