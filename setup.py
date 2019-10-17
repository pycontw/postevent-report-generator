#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="attendees-analyzer",
    packages=find_packages(),
    zip_safe=False,
    version="0.0.1",
    description="To analyze attendee data",
    author="Taihsiang Ho (tai271828)",
    author_email="tai271828@gmail.com",
    url="https://github.com/tai271828/attendees-analyzer",
    download_url="https://github.com/tai271828/attendees-analyzer",
    keywords=["attendee", "pycontw"],
    entry_points={"console_scripts": ["rg-cli=atta.controller.atta_cli:main"]},
    classifiers=["Programming Language :: Python"],
)
