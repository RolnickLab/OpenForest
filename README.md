# OpenForest

![openforest_logo](./images/logo_wo_background.png)

OpenForest is an initiative to centralize open source forest monitoring dataset. This repository is open to contributions.
It has been motivated by our work **OpenForest: review and challenges of open source forests datasets** (link will be provided soon).

Each the datasets listed in OpenForest follows these critera which are discussed in the corresponding article. If you want to add a new dataset, please ensure that it follows the same criteria before proceeding to the next stage.

- The dataset should be open source, *i.e.* without any request requirement;
- The dataset should be related to at least one published article, exceptions have been made for datasets that are available as preprints, but are considered to be must-see datasets;
- The dataset should be focused on the composition of the forest, excluding event-based specific ones (*i.e.* wildfires detection);
- A land use and/or land cover (LULC) dataset should contain more than a single `forest' class since a focus is made on better understanding the composition of the forest;
- The dataset should be at the tree level at least, excluding datasets at the organ or cellular level considered as out of the scope of this review (*e.g.* leaf spectra, root scans, dendro computer tomography)
- The dataset should contained at least $O(1000)$ trees.

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
- Todo 1
- Todo 2
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

6. Commit your changes and push it to your branch:
```bash
$ cd ..
$ git add .
$ git commit -m "meaningful commit message"
$ git push origin my-branch
```

7. Create a new Pull Request on the Github webpage of the repo. It will be validated and merged to the main branch as soon as possible if it fits the requirements and passes the tests.


---

## How to modify OpenForest?

This is under construction.

---

#### To-do list

- [ ] Add another database for forest data providers.
- [ ] Add a Python counter to display the current number of datasets in the README.
- [ ] Add a Python function to integrate a dynamic visualization of the geographic distribution of the datasets.
- [ ] Integrate Travis or CircleCI for automatic test running.