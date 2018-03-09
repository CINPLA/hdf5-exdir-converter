# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

install_requires = []

entry_points = {
    'console_scripts': [
        'hdf5_exdir_converter=hdf5_exdir_converter.main:main'
    ]}

setup(
    name="hdf5_exdir_converter",
    version=1.0,
    author='Milad H. Mobarhan',
    author_email='m@milad.no',
    license="GPLv3",
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
)
