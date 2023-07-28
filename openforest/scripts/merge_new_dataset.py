import argparse
import yaml
import pandas as pd

from openforest.utils import OPENFOREST_HOME

def load_dataset_file(path):
    with open(path, 'r') as stream:
        try:
            dataset_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dataset_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', help='Name of the YAML file describing the dataset', required=True)
    args = vars(parser.parse_args())
    file_path = OPENFOREST_HOME / args['dataset_name']
    dataset_file = load_dataset_file(file_path)
    new_dataset = pd.DataFrame([dataset_file])
    new_dataset.set_index('dataset_name', inplace=True)
    openforest = pd.read_csv(OPENFOREST_HOME.parent / 'OpenForest.csv', index_col='dataset_name')
    updated_openforest = pd.concat([openforest, new_dataset])
    #TODO: write new open foresst / remove the temp dataset file
    import ipdb; ipdb.set_trace()
    
if __name__ == '__main__':
    main()
