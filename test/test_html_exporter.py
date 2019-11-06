from hypothesis import given
from hypothesis import strategies as st
from hypothesis.provisional import urls

from report_generator.exporter import html


class TestGenerateHtmlRow:
    @given(st.text())
    def test_single_row(self, row):
        assert html._generate_html_rows(row) == f"<td>{row}</td>"

    @given(st.lists(st.text()))
    def test_multiple_rows(self, rows):
        expected = "".join([f"<td>{row}</td>" for row in rows])
        assert html._generate_html_rows(*rows) == expected


class TestGenerateHtmlLink:
    @given(urls())
    def test_url(self, link):
        assert html._generate_html_link(link) == f"<a href={link}>{link}</a>"
