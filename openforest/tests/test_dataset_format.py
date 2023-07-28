import argparse
import sys
import yaml
import pandas as pd
from pytest import fixture

from openforest.utils import OPENFOREST_HOME

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', help='Name of the YAML file describing the dataset', required=True)
    return parser.parse_args(args)


@fixture
def dataset():
    dataset_name = parse_args(sys.argv[1:])
    with open(path, 'r') as stream:
        try:
            dataset_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dataset_file

def test_len(dataset):
    assert len(dataset) == 14

# def main():   
    # import ipdb; ipdb.set_trace()
    
# if __name__ == '__main__':
    # main()
