#!/usr/bin/env python3
import pytest

from report_generator.partner import sponsor


class TestSponsor:
    @pytest.fixture(scope="class")
    def sponsors(self):
        return sponsor.get_all_sponsors(
            "tests/data/packages.yaml", "tests/data/sponsors.yaml"
        )

    @pytest.fixture(scope="class")
    def platinum_partner(self, sponsors):
        return [sponsor for sponsor in sponsors if sponsor.name == "PSF"][0]

    def test_sponsor_number(self, sponsors):
        assert len(sponsors) == 1

    def test_sponsor_name(self, platinum_partner):
        assert platinum_partner.name == "PSF"

    def test_sponsor_promotion_web_click(self, platinum_partner):
        assert platinum_partner.web_click == 999

    def test_sponsor_promotion_web_click_rank_platinum(self, platinum_partner):
        assert platinum_partner.web_click_rank == 1

    @pytest.mark.skip("No bronze sponsor in test case")
    def test_sponsor_promotion_web_click_rank_bronze(self):
        answer = sponsor.NA_CONTENT_MESSAGE
        self.assertEqual(self.bronze_sponsor.web_click_rank, answer)

    @pytest.mark.skip("No bronze sponsor in test case")
    def test_sponsor_promotion_fb_len(self):
        self.assertEqual(len(self.platinum_partner.facebook_url), 3)

    @pytest.mark.skip("No bronze sponsor in test case")
    def test_sponsor_promotion_fb_url_reach(self):
        url_link = "https://www.facebook.com/pycontw/posts/1657384737713695"
        target_url = self.platinum_partner.facebook_url[url_link]
        self.assertEqual(target_url["reach"], 1000)

    @pytest.mark.skip("No bronze sponsor in test case")
    def test_sponsor_promotion_fb_url_engagement(self):
        url_link = "https://www.facebook.com/pycontw/posts/1657384737713695"
        target_url = self.platinum_partner.facebook_url[url_link]
        self.assertEqual(target_url["engagement"], 2000)
