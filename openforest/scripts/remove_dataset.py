import argparse
import yaml
import pandas as pd

from openforest.scripts.openforest_database import OpenForestDatabase
from openforest.utils import OPENFOREST_HOME
from openforest.utils.functions import get_dataset_name, load_dataset_name

def main():
    args = get_dataset_name()
    file_path = OPENFOREST_HOME / args['dataset_name']
    dataset_file = load_dataset_file(file_path)
    database = OpenForestDatabase()
    database.add_row(dataset_file)
    database.erase
    
if __name__ == '__main__':
    main()
