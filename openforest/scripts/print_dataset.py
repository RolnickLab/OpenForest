import argparse
import yaml
import pandas as pd

from openforest.scripts.openforest_database import OpenForestDatabase
from openforest.utils import OPENFOREST_HOME
from openforest.utils.functions import get_dataset_name

def main():
    args = get_dataset_name()
    dataset_name = args['dataset_name']
    database = OpenForestDatabase()
    database.print_row(dataset_name)
    database.print_url(dataset_name)


if __name__ == '__main__':
    main()
