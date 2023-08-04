"""
pytest --dataset_name='PULL_REQUEST_TEMPLATE.yml' test_dataset_format.py
"""
import yaml
import pandas as pd
import geopandas as gpd
import pytest
from pytest import fixture
from datetime import datetime

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

def test_len(new_dataset):
    assert len(new_dataset) == 14, 'The provided dataset file does not contain enough criteria. '\
        'Please refer to the template provided in the repo.'

def test_index(new_dataset):
    dataset = pd.DataFrame([new_dataset])
    try:
        dataset.set_index('dataset_name', inplace=True)
    except:
        KeyError('The dataset_name attribute is required.')

def test_in_article(new_dataset):
    assert new_dataset['in_article'] == False, "The in_article attribute should be set to 'No' or 'False'"

def test_category(new_dataset):
    for _, letter in enumerate(new_dataset['category']):
        assert letter in ('I', 'G', 'A', 'S', 'M'), 'The category letter is not set propertly. '\
            'Please refer to the template and the README of the repo.'
    
def test_year_publication(new_dataset):
    assert len(str(new_dataset['year_publication'])) == 4, 'Year of publication is not in the correct format.'
    assert 1970 <= new_dataset['year_publication'] <= datetime.today().year+1, 'Year of publication is not valid.'

def test_year_recordings(new_dataset):
    recording_years = new_dataset['year_recordings']
    if isinstance(recording_years, int):
        assert len(str(recording_years)) == 4, 'Year of publication is not in the correct format.'
        # Note that year+1 is tolerated for the publication year
        assert 1970 <= recording_years <= datetime.today().year+1, 'Year of publication is not valid.'
    else:
        recording_years = recording_years.split('/')
        for _, years in enumerate(recording_years):
            years = years.split('-')
            assert len(years[0]) == 4, 'Year of publication is not in the correct format.'
            assert 1970 <= int(years[0]) <= datetime.today().year, 'Year of publication is not valid.'
            if len(years) > 1:
                assert len(years[1]) == 4, 'Year of publication is not in the correct format.'
                assert 1970 <= int(years[1]) <= datetime.today().year, 'Year of publication is not valid.'
                assert int(years[0]) < int(years[1]), 'First year should be < to second year in time series.'

def test_volume(new_dataset):
    # TODO: tests TBD
    pass

def test_data_resolution(new_dataset):
    dataset = pd.DataFrame([new_dataset])
    dataset.set_index('dataset_name', inplace=True)
    modalities = dataset['data'].str.split(', ')
    resolutions = dataset['resolution'].str.split(', ')
    assert len(modalities) == len(resolutions), 'Each data modality should be associated to a resolution. '\
        'Please refer to the template and the README of the repo.'

def test_time_series(new_dataset):
    is_time_series = new_dataset['time_series']
    recording_years = new_dataset['year_recordings']
    if isinstance(recording_years, int):
        assert is_time_series == False, "The time_series attribute should be set to 'No' or 'False'"
    else:
        recording_years = recording_years.split('/')
        detected_time_series = False
        for _, years in enumerate(recording_years):
            if '-' in years:
                assert is_time_series == True, "The time_series attribute should be set to 'Yes' or 'True'"
                detected_time_series = True
        if detected_time_series == False:
            assert is_time_series == False, "The time_series attribute should be set to 'No' or 'False'"

def test_potential_tasks(new_dataset):
    # This list should be updated if a new task is introduced
    task_list = ['Align.', 'CD', 'Classif.', 'IS', 'KD', 'MC', 'OD', 'OL', 'Reg.', 'Seg.']
    tasks = new_dataset['potential_tasks'].split(', ')
    for task in tasks:
        assert task in task_list

def test_nb_classes(new_dataset):
    nb_classes = new_dataset['nb_classes']
    tasks = new_dataset['potential_tasks'].split(', ')
    is_classif = False
    for task in tasks:
        if task in ['Classif.', 'Seg.', 'OD', 'IS', 'MC']: # Note this list can change
            # Note that text can be included in this column
            # It cannot be tested with integer values.
            assert nb_classes != 'N/A', 'Regarding the potential_tasks attribute, a number of classes should be mentioned'
            is_classif = True
    if is_classif == False:
        assert nb_classes == 'N/A', "Regarding the potential_tasks attribute, the number of classes should be set to 'N/A'"

def test_location(new_dataset):
    # TODO: be less restrictive in case location are not in the list
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    locations = new_dataset['location'].split(', ')
    for location in locations:
        checker = world.name.str.find(location).unique()
        assert 0 in checker, 'The provided location: {} is not in the GeoPandas world country list'.format(location)

def test_url(new_dataset):
    # TODO: tests TDB
    pass

def test_license(new_dataset):
    # TODO: tests TDB
    pass
