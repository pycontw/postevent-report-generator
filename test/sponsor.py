#!/usr/bin/env python3
import unittest
from atta.partner import sponsor


class TestSponsor(unittest.TestCase):

    def test_attributes(self):
        sponsors = sponsor.get_all_sponsors()
        self.assertEqual(len(sponsors), 2)


if __name__ == '__main__':
    unittest.main()
