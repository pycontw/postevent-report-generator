#!/usr/bin/env python3
import csv
import unittest
from atta.cleaner.title import cat_title


class TestTitleCategory(unittest.TestCase):

    def test_mapping(self):
        with open('./data/title-category.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertEqual(cat_title(row['QUESTION']), row['ANSWER'])


if __name__ == '__main__':
    unittest.main()
