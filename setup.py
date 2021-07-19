#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name='rki-data-analyzer',
    version='1.1',
    packages=['rki_data_analyzer'],
    url='https://github.com/codemonkey500',
    license='',
    author='codemonkey500',
    author_email='',
    description='Tool for analyzing RKI Covid-19 data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["setuptools>=49.2.1", "pandas>=1.2.0",
                      "matplotlib>=3.3.3", "requests>=2.25.1"]
)
