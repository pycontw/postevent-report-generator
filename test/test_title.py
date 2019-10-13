#!/usr/bin/env python3
import csv
from atta.cleaner.title import cat_title


class TestTitleCategory:
    def test_mapping(self):
        with open("test/data/title-category.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                assert cat_title(row["QUESTION"]) == row["ANSWER"]