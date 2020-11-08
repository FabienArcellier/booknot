#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='booknot',
    version='0.0.1',
    packages=find_packages(exclude=["*_tests"]),
    license='MIT license',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_data={
        'configuration': ['booknot/resources/*'],
    },
    entry_points = {
        'console_scripts': [
            'booknot = booknot.cli:cli',
        ],
    },
    install_requires = [
        'attrs',
        'beautifulsoup4',
        'click',
        'decorator',
        'jinja2',
        'requests'
    ],
    extras_require={
        'dev': [
            'pylint',
            'coverage',
            'tox',
            'twine'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Environment :: Console"
    ]
)
