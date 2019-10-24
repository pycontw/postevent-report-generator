#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="PyCon TW post-event report generator",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    version="0.0.2",
    description="A cli command to generate PyCon TW post-event reports. Previously known as attendee-analyzer",
    author="Taihsiang Ho (tai271828)",
    author_email="tai271828@gmail.com",
    url="https://github.com/tai271828/pycontw-postevent-report-generator",
    download_url="https://github.com/tai271828/pycontw-postevent-report-generator",
    keywords=["attendee", "pycontw", "post-event"],
    entry_points={"console_scripts": ["rg-cli=report_generator.controller.report_generator_cli:main"]},
    classifiers=["Programming Language :: Python"],
)
