#! /usr/bin/env python3
from setuptools import setup

import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name                =   "vulnScan",
    version             =   '1.0',
    description         =   "The Multi-Tool Web Vulnerability Scanner.",
    long_description    =   README,
    long_description_content_type = "text/markdown",
    url                 =   "",
    author              =   "gowtham",
    py_modules          =   ['vulnscan',],
    install_requires    =   [],
    python_requires=">=3.6",
)
