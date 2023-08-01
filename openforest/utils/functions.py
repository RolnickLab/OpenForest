import argparse

def get_dataset_name(path):
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', help='Name of the YAML file describing the dataset', required=True)
    args = vars(parser.parse_args())
    return args
