#!/usr/bin/env python3
import unittest
from atta.partner import sponsor


class TestSponsor(unittest.TestCase):
    def setUp(self):
        sponsors = sponsor.get_all_sponsors('./data/packages.yaml',
                                            './data/sponsors.yaml')
        self.sponsors = sponsors

        for spartner in sponsors:
            if spartner.name == 'Gandi':
                self.platinum_partner = spartner

        for spartner in sponsors:
            if spartner.name == 'Carousell':
                self.bronze_sponsor = spartner

    def test_sponsor_number(self):
        self.assertEqual(len(self.sponsors), 4)

    def test_sponsor_name(self):
        self.assertEqual(self.platinum_partner.name, 'Gandi')

    def test_sponsor_promotion_web_click(self):
        self.assertEqual(self.platinum_partner.web_click, 600)

    def test_sponsor_promotion_web_click_rank_platinum(self):
        self.assertEqual(self.platinum_partner.web_click_rank, 1)

    def test_sponsor_promotion_web_click_rank_bronze(self):
        answer = sponsor.NA_CONTENT_MESSAGE
        self.assertEqual(self.bronze_sponsor.web_click_rank, answer)

    def test_sponsor_promotion_fb_len(self):
        self.assertEqual(len(self.platinum_partner.facebook_url), 3)

    def test_sponsor_promotion_fb_url_reach(self):
        url_link = 'https://www.facebook.com/pycontw/posts/1657384737713695'
        target_url = self.platinum_partner.facebook_url[url_link]
        self.assertEqual(target_url['reach'], 1000)

    def test_sponsor_promotion_fb_url_engagement(self):
        url_link = 'https://www.facebook.com/pycontw/posts/1657384737713695'
        target_url = self.platinum_partner.facebook_url[url_link]
        self.assertEqual(target_url['engagement'], 2000)


if __name__ == '__main__':
    unittest.main()
