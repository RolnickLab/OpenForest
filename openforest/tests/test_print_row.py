"""
pytest --dataset_name='test_dataset_example.yml' test_modify_row.py
"""
import yaml
import pandas as pd
import pytest
from pytest import fixture

from openforest.scripts.openforest_database import OpenForestDatabase


def test_print_row():
    openforest = OpenForestDatabase()
    openforest.print_row('Cactus Aerial Photos')

if __name__ == '__main__':
    test_print_row()
