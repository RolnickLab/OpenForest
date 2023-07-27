"""Script to clean the database which includes latex commands"""
import pandas as pd
from openforest.utils import OPENFOREST_HOME

def load():
    database = pd.read_csv(OPENFOREST_HOME.parent / 'OpenForest.csv',
                           index_col='dataset_name')
    return database
    
def clean(database):
    for col_name, values in database.items():
        if col_name in ('volume', 'data', 'resolution', 'potential_tasks',  'nb_classes', 'location',
                        'url', 'license'):
            new_values = values.fillna('N/A')
            new_values = new_values.apply(lambda x: x.replace(' \\newline ', ', '))
            new_values = new_values.apply(lambda x: x.replace(' \\times ', 'x'))
            new_values = new_values.apply(lambda x: x.replace('$', ''))
            new_values = new_values.apply(lambda x: x.replace('^{\\circ}', 'deg'))
            new_values = new_values.apply(lambda x: x.replace('\\href{', ''))
            new_values = new_values.apply(lambda x: x.replace('}{data}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{dataset}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{data1}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{data2}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{data3}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{visu}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{page}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{Specific}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{specific}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{Community Data License Agreement – Permissive, Version 1.0}', ''))
            new_values = new_values.apply(lambda x: x.replace('}{Open Data Commons Open Database License (ODbL)}', ''))
            database[col_name] = new_values
    return database

def save(cleaned_database):
    cleaned_database.to_csv(OPENFOREST_HOME.parent / 'OpenForest_cleaned.csv')
    
def main():
    database = load()
    cleaned_database = clean(database)
    save(cleaned_database)

if __name__=='__main__':
    main()
