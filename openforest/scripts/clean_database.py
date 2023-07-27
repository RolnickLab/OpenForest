import pandas as pd
from openforest.utils import OPENFOREST_HOME

def load():
    import ipdb; ipdb.set_trace()
    database = pd.read_csv(OPENFOREST_HOME / 'OpenForest.csv')
    # set name as index
    return database
    
def clean(database):
    import ipdb; ipdb.set_trace()

def main():
    database = load()

if __name__=='__main__':
    main()
