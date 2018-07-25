#!/usr/bin/env python3
import unittest
from atta.partner import sponsor


class TestSponsor(unittest.TestCase):
    def setUp(self):
        sponsors = sponsor.get_all_sponsors('./data/packages.yaml',
                                            './data/sponsors.yaml')
        self.sponsors = sponsors

    def test_sponsor_number(self):
        self.assertEqual(len(self.sponsors), 2)

    def test_sponsor_attributes(self):
        for sponsor in self.sponsors:
            if sponsor.name == 'Gandi':
                target_sponsor = sponsor

        self.assertEqual(target_sponsor.name, 'Gandi')


if __name__ == '__main__':
    unittest.main()
