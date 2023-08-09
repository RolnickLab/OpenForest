# OpenForest

![openforest_logo](./images/logo_wo_background.png)

OpenForest is an initiative to centralize open source forest monitoring dataset. This repository is open to contributions.
It has been motivated by our work **OpenForest: review and challenges of open source forests datasets** (link will be provided soon).

Each the datasets listed in [OpenForest](./OpenForest.csv) follows these critera which are discussed in the corresponding article. If you want to add a new dataset, please ensure that it follows the same criteria before proceeding to the next stage.

- The dataset should be open source, *i.e.* without any request requirement;
- The dataset should be related to at least one published article, exceptions have been made for datasets that are available as preprints, but are considered to be must-see datasets;
- The dataset should be focused on the composition of the forest, excluding event-based specific ones (*i.e.* wildfires detection);
- A land use and/or land cover (LULC) dataset should contain more than a single `forest' class since a focus is made on better understanding the composition of the forest;
- The dataset should be at the tree level at least, excluding datasets at the organ or cellular level considered as out of the scope of this review (*e.g.* leaf spectra, root scans, dendro computer tomography)
- The dataset should contained at least $O(1000)$ trees.

The OpenForest database is available in this repo [here](./OpenForest.csv).

---

## Preliminary steps

1. Clone the repo:
```bash
$ git clone https://github.com/RolnickLab/OpenForest.git
```

2. Install the repo using pip:
```bash
$ cd OpenForest/
$ pip install -e .
```
The pip installation will include all the dependencies of the [requirements](./requirements.txt) file. if not, you should install these dependancies manually using pip or conda.
With this, you can edit the OpenForest code on the fly and import function and classes of OpenForest in other project as well.

---

## How to add a new dataset?

1. Create a new dataset file from the proposed [template](./openforest/PULL_REQUEST_TEMPLATE.yml) `PULL_REQUEST_TEMPLATE.yml`.
```bash
$ cd OpenForest/
$ cp openforest/PULL_REQUEST_TEMPLATE.yml openforest/NEW_DATASET.yml
```

2. Edit the dataset file as you want while respecting the following typos for each attribute:
- `dataset_name`: name of your dataset, ensure that it is not already existing.
- `in_article`: if your dataset is not part of our main article, set it to `No` or `False`.
- `category`: depending on the modality available in your dataset, please indicate one or several letters as following: `I` for inventories, `G` for ground-based recordings, `A` for aerial recordings, `S` for satellite recordings, `M` for maps. For more information, please refer to our article.
- `year_publication`: indicate the year of the associated publication or preprint release.
- `year_recordings`: indicate each year of data recording separated by `/`, *e.g.* `2019/2020`. If you want to indicate a time series, separate the two date bounds by `-`, *e.g.* `2010-2020`. You can include both time series and single dates such as `2009/2010-2020/2021`. Note that `Unknown` is a valid entry if the recording date is not available.
-`volume`: TODO
- `data`: TODO
- `resolution`: TODO
- `time_series`: TODO
- `potential_tasks`: TODO
- `nb_classes`: TODO
- `location`: TODO
- `url`: TODO
- `license`: TODO
Note that the file will be tested before merging to ensure that the format and typos are respected.

3. Run tests locally to ensure the format of the file:
```bash
$ cd openforest/
$ bash tests/run_tests_to_add.sh NEW_DATASET.yml
```

4. Create your branch:
```bash
$ git checkout -b my-branch
```

5. Update OpenForest with your new dataset and delete your YAML file after verifying that the update has been correctly done:
```bash
$ python3 scripts/add_new_dataset.py --dataset_name='NEW_DATASET.yml'
$ rm NEW_DATASET.yml
```

6. Commit your changes, push it to your branch and create a Pull Request:
```bash
$ cd ..
$ git add .
$ git commit -m "meaningful commit message"
$ git push origin my-branch
```
Create a new Pull Request on the Github webpage of the repo. It will be validated and merged to the main branch as soon as possible if it fits the requirements and passes the tests.


---

## How to modify and explore OpenForest

After any step of this section, you can push your changes and create a pull request according to step 4.

1. Modify a dataset

If you want to modify the content of a dataset row in OpenFoest, you need a dedicated YAML file [template](./openforest/PULL_REQUEST_TEMPLATE.yml) including both the existing and updated information.
Note that the `dataset_name` attribute should match with an existing one in OpenForest.
First run the following test with the corresponding YAML file `MODIFIED_DATASET.yml`:
```bash
$ cd openforest/
$ bash tests/run_tests_to_modify.sh 'MODIFIED_DATASET.yml'
```

If you pass the tests, run the following command line to remove the dataset, update OpenForest and delete your YAML file:
```bash
$ python3 scripts/modify_dataset.py --dataset_file='MODIFIED_DATASET.yml'
$ rm MODIFIED_DATASET.yml
```

2. Remove a dataset

If you want to delete a dataset in OpenForest, you only need the name of your dataset.
First, run the following test:
```bash
$ cd openforest/
$ bash tests/run_tests_to_remove.sh 'Name of your dataset'
```

If you pass the tests, run the following command line to remove the dataset and update OpenForest:
```bash
$ python3 scripts/remove_dataset.py --dataset_name='Name of your dataset'
```

3. Print the dataset row and URL(s) to access it:

You can print the dataset information, including the URL(s) to access it using the following command line:
```bash
$ cd openforest/
$ python3 scripts/print_dataset.py --dataset_name='Name of your dataset'
```

4. Commit your changes, push it to your branch and create a Pull Request:
```bash
$ cd ..
$ git add .
$ git commit -m "meaningful commit message"
$ git push origin my-branch
```
Create a new Pull Request on the Github webpage of the repo. It will be validated and merged to the main branch as soon as possible if it fits the requirements and passes the tests.


---

#### To-do list

- [ ] Add another database for forest data providers.
- [ ] Add a Python counter to display the current number of datasets in the README.
- [ ] Add a Python function to integrate a dynamic visualization of the geographic distribution of the datasets.
- [ ] Integrate Travis or CircleCI for automatic test running.