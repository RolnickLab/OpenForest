import os
from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='OpenForest',
      version='0.1.0',
      license='Apache 2.0',
      author='Arthur Ouaknine',
      url='https://github.com/RolnickLab/OpenForest.git',
      packages=find_packages(),
      install_requires=required)
