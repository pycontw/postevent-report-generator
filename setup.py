#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="pycontw-report-generator",
    packages=["report_generator"],
    zip_safe=False,
    include_package_data=True,
    version="1.0.0",
    description="PyCon TW post-event report generator.A cli command to generate PyCon TW post-event reports. Previously known as attendee-analyzer",
    author="Taihsiang Ho (tai271828)",
    author_email="tai271828@gmail.com",
    url="https://github.com/pycontw/pycontw-postevent-report-generator",
    download_url="https://github.com/pycontw/pycontw-postevent-report-generator.git",
    keywords=["attendee", "pycontw", "post-event", "report-generator"],
    entry_points={"console_scripts": ["rg-cli=report_generator.controller.report_generator_cli:main"]},
    install_requires=[
        "pandas", "seaborn", "numpy", "matplotlib", "click",
        "Pillow", "Jinja2", "PyYAML"
    ],
    classifiers=["Programming Language :: Python"],
)
