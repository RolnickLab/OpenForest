"""The OpenForest Database"""
import pandas as pd
import yaml

from openforest.utils import OPENFOREST_HOME

class OpenForestDatabase:

    def __init__(self):
        openforest_path = OPENFOREST_HOME.parent / 'OpenForest.csv'
        self.database = pd.read_csv(OPENFOREST_HOME.parent / 'OpenForest.csv', index_col='dataset_name')

    def __len__(self):
        return len(self.database)

    def add_row(self, new_dataset):
        new_dataset = pd.DataFrame([new_dataset])
        new_dataset.set_index('dataset_name', inplace=True)
        self.database = pd.concat([self.database, new_dataset])

    def delete_row(self, dataset_name):
        self.database.drop(dataset_name, axis='index', inplace=True)

    def modify_row(self, modified_dataset):
        # Modify a row still require a YAML file with an existing dataset name in OpenForest
        dataset_name = modified_dataset['dataset_name']
        self.delete_row(dataset_name)
        self.add_row(modified_dataset)

    def print_row(self, dataset_name=None):
        if dataset_name:
            print(self.database.loc[dataset_name])
        else:
            print(self.database)

    def print_url(self, dataset_name):
        print("URL(s) to access the '{}' dataset: {}.".format(dataset_name,
                                                              self.database.loc[dataset_name]['url']))

    @property
    def erase(self):
        self.database.to_csv(OPENFOREST_HOME.parent / 'OpenForest_test.csv')
    
    @property
    def get(self):
        return self.database
