import argparse
import yaml

def get_dataset_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_file', help='Name of the YAML file describing the dataset', required=True)
    args = vars(parser.parse_args())
    return args

def get_dataset_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', help='Name of the dataset', required=True)
    args = vars(parser.parse_args())
    return args

def load_dataset_file(path):
    with open(path, 'r') as stream:
        try:
            dataset_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dataset_file
