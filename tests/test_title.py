#!/usr/bin/env python3
import csv

from report_generator.cleaner.title import cat_title


class TestTitleCategory:
    def test_mapping(self):
        with open("tests/data/title-category.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                assert cat_title(row["QUESTION"]) == row["ANSWER"]
