#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo "Path to the YAML dataset file is mandatory, please add it as parameter of the script."
    exit 1
fi

echo "Path to the YAML dataset file -> " $1

pytest --dataset_file=$1 tests/test_dataset_format.py && pytest --dataset_file=$1 tests/test_modify_row.py
