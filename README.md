# OpenForest

![openforest_logo](./images/logo_wo_background.png)

OpenForest is an initiative to centralize open access forest monitoring datasets. This repository is open to contributions.
It has been motivated by our work **OpenForest: A data catalogue for machine learning in forest monitoring** (link will be provided soon).

Each the datasets listed in [OpenForest](./OpenForest.csv) follows these critera which are discussed in the corresponding article. If you want to add a new dataset, please ensure that it follows the same criteria before proceeding to the next stage.

- The dataset should be open access, *i.e.* without any request requirement;
- The dataset should be related to at least one published article, exceptions have been made for datasets that are available as preprints, but are considered to be must-see datasets;
- The dataset should be focused on the composition of the forest, excluding event-based specific ones (*i.e.* wildfires detection);
- A land use and/or land cover (LULC) dataset should contain more than a single plant functional type (*i.e.* conifers or deciduous) since a focus is made on better understanding the composition of the forest;
- The dataset should be at the tree level at least, excluding datasets at the organ or cellular level considered as out of the scope of this review (*e.g.* leaf spectra or root scans)
- The dataset should contained at least $O(1000)$ trees.

The OpenForest catalogue is available in this repo [here](./OpenForest.csv).

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
- `article_url`: indicate the url to the article associated to your dataset. If your dataset is included in our initial work and thus accessible in our article, this attribute will be set to `False`.
- `category`: depending on the modality available in your dataset, please indicate one or several letters as following: `I` for inventories, `G` for ground-based recordings, `A` for aerial recordings, `S` for satellite recordings, `M` for maps. For more information, please refer to our article.
- `year_publication`: indicate the year of the associated publication or preprint release.
- `year_recordings`: indicate each year of data recording separated by `/`, *e.g.* `2019/2020`. If you want to indicate a time series, separate the two date bounds by `-`, *e.g.* `2010-2020`. You can include both time series and single dates such as `2009/2010-2020/2021`. Note that `Unknown` is a valid entry if the recording date is not available.
- `dataset_size`: depending on the modalities available in the dataset, please indicate the number of trees, number of samples, number of maps with the appropriate order of magnitude, *i.e* `k` for thousands, `M` for millions, `B`for billions. You can also indicate the area covers by the provided data with an appropriate order of magnitude, either `ha` or `km2`. Please separate each element with a coma and a space: `, `.
- `data`: indicate each modality available in your dataset *e.g.* `Aerial RGB`, `Multispectral`, `SAR`, `LiDAR PC` and so on. You can refer to our article, to the existing examples in OpenForest and to the pull request YAML file template for more details on the required formats.
- `spatial_resolution_or_precision`: according to the same order than in the `data` attribute, indicate the associated spatial resolution or precision of each modality provided in the dataset. The measure unit depends on the modality, *e.g.* centimeters, meters, kilometers or number of points per meter squared for point clouds. Please separate each element withe coma and a space: `, `.
- `time_series`: indicate `Yes` or `No`if your dataset contains a time series, note that it must be consistant with the `year_recordings` attribute.
- `potential_tasks`: indicate the potential tasks that your dataset could be used for. It should belongs to the following list: `Align.`: alignment, `CD`: change detection, `Classif.`: classification, `IS`; instance segmentation, `KD`: key-point detection, `MC`: multi classification, `OD`: object detection, `OL`: object localization, `Reg.`: regression, `Seg.`: semantic segmentation. You can also push a new task with a pool request modifying the corresponding test after validation by an admnistrator. Please separate each element with a coma and a space: `, `.
- `nb_classes`: indicate the number of classes in your datasets if applicable, `N/A` otherwise. You can also indicates the number of classes per `species`, `genus` and `family` while separating each element with a coma and a space: `, `.
- `location`: indicate the countries in which your dataset is localized. The name of the countries should follow the `naturalearth_lowres` formatting from `geopandas`. It can be accessed by using the following command line: `geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))`. If your dataset is at the continent or world level, you can either indicate the name of the continent or `Worldwide`. Please separate each element with a coma and a space: `, `.
- `url`: indate the url(s) to access your dataset. Please separate each element with a coma and a space: `, `.
- `license`: indicate the license application to your dataset.
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
$ python scripts/add_new_dataset.py --dataset_file='NEW_DATASET.yml'
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
$ python scripts/modify_dataset.py --dataset_file='MODIFIED_DATASET.yml'
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
$ python scripts/remove_dataset.py --dataset_name='Name of your dataset'
```

3. Print the dataset row and URL(s) to access it:

You can print the dataset information, including the URL(s) to access it using the following command line:
```bash
$ cd openforest/
$ python scripts/print_dataset.py --dataset_name='Name of your dataset'
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

## How to add, modify or delete a data provider?

**This section is under construction**

---

#### To-do list

- [X] Add another database for forest data providers.
- [ ] Write tests and script to add, modify and delete data providers (+ associated doc)
- [ ] Add a Python counter to display the current number of datasets in the README.
- [ ] Add a Python function to integrate a dynamic visualization of the geographic distribution of the datasets.
- [ ] Integrate Travis or CircleCI for automatic test running.
