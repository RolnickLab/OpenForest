#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo "Name of the dataset file to remove is mandatory, please add it as parameter of the script."
    exit 1
fi

echo "Name of the dataset to remove -> " $1

pytest --dataset_name="$1" tests/test_delete_row.py
