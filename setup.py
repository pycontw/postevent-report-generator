#!/usr/bin/env python3
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "docs/README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="pycontw-report-generator",
    packages=find_packages(exclude=["tasks", "test", "scripts"]),
    zip_safe=False,
    include_package_data=True,
    version="1.1.0",
    description="PyCon TW post-event report generator.A cli command to generate PyCon TW post-event reports.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Taihsiang Ho (tai271828)",
    author_email="tai271828@gmail.com",
    license="BSD 3-Clause",
    url="https://github.com/pycontw/pycontw-postevent-report-generator",
    download_url="https://github.com/pycontw/pycontw-postevent-report-generator.git",
    keywords=["attendee", "pycontw", "post-event", "report-generator"],
    entry_points={
        "console_scripts": [
            "rg-cli=report_generator.controller.report_generator_cli:main"
        ]
    },
    install_requires=[
        "pandas",
        "seaborn",
        "numpy",
        "matplotlib",
        "click",
        "Pillow",
        "Jinja2",
        "PyYAML",
    ],
    classifiers=["Programming Language :: Python"],
)
