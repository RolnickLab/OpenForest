"""
pytest --dataset_name='PULL_REQUEST_TEMPLATE.yml' test_merge.py
"""
import yaml
import pandas as pd
import pytest
from pytest import fixture

from openforest.utils import OPENFOREST_HOME

@fixture
def new_dataset(dataset_name):
    path = OPENFOREST_HOME / dataset_name
    with open(path, 'r') as stream:
        try:
            dataset_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dataset_file

def test_matching(new_dataset):
    openforest = pd.read_csv(OPENFOREST_HOME.parent / 'OpenForest.csv', index_col='dataset_name')
    new_dataset = pd.DataFrame([new_dataset])
    assert 'dataset_name' in new_dataset.columns, 'The dataset_name attribute is required. '\
        'Please refer to the template provided in the repo.'
    new_dataset.set_index('dataset_name', inplace=True)
    assert len(list(openforest.columns)) == len(list(new_dataset.columns)), 'The number of attributes provided is not correct. '\
        'Please refer to the template provided in the repo.'
    assert list(openforest.columns) == list(new_dataset.columns), 'The attributes are not identical to the pull request template. '\
        'Please refer to the template provided in the repo.'

def test_merging(new_dataset):
    openforest = pd.read_csv(OPENFOREST_HOME.parent / 'OpenForest.csv', index_col='dataset_name')
    new_dataset = pd.DataFrame([new_dataset])
    new_dataset.set_index('dataset_name', inplace=True)
    try:
        updated_openforest = pd.concat([openforest, new_dataset])
    except:
        print('Error merging the new dataset with OpenForest.')
    assert len(updated_openforest) == len(openforest)+1
